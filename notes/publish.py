import os
import shutil
import re
import sys
import json

DEPENDENCIES = {"Excalidraw": [".svg"], "Assets": [".jpg"]}
# PUBVAULT = "C:/Users/shameel/Documents/public-notes"
ROOT = "../"
PUBLISH_FOLDER = "../content"
TIKZ_JSON = "tikzdiagrams.json"
WINDOWS_LINE_ENDING = b"\r\n"
UNIX_LINE_ENDING = b"\n"

tikzdiagrams = {}
diagramticker = 0

if not os.path.isfile(TIKZ_JSON):
    with open(TIKZ_JSON, "w", encoding="utf-8") as f:
        json.dump({}, f)

with open(TIKZ_JSON, "r", encoding="utf-8") as f:
    tikzdiagrams = json.load(f)


def getroots():
    try:
        with open(".publish", "r", encoding="ascii") as f:
            lines = [line.strip() for line in f if line.strip()]
            return lines
    except FileNotFoundError as e:
        print(f"error {e}")
        return []


def checkvalid(paths):
    return all(os.path.isdir(p) for p in paths)


def createtikzdiagram(match):
    global diagramticker
    diagramticker += 1
    content = (
        "\\documentclass[tikz,convert={outfile=\\jobname.svg}]{standalone}\n"
        + match.group(1)
    )

    diagramname = f"tikzdiagram{diagramticker}.svg"
    if content in tikzdiagrams:
        with open(
            os.path.join(PUBLISH_FOLDER, "SVG", diagramname), "w", encoding="utf-8"
        ) as f:
            f.write(tikzdiagrams[content])
        return f"![[SVG/{diagramname}|diagram]]"

    # Generate the diagram tikz
    with open(".pdf2svg/svg.tex", "w", encoding="utf-8") as f:
        f.write(content)
    os.chdir(".pdf2svg")
    os.system("pdflatex svg.tex")
    os.system("pdf2svg svg.pdf out.svg")
    os.chdir("..")
    with open(".pdf2svg/out.svg", "r", encoding="utf-8") as f:
        tikzdiagrams[content] = f.read()

    diagrampath = f"{PUBLISH_FOLDER}/SVG/{diagramname}"
    shutil.copy2(".pdf2svg/out.svg", diagrampath)
    return f"![[SVG/{diagramname}|diagram]]"


def applytransform(text):
    # This regex matches ```tikz\n...```
    tikzpattern = r"```tikz\n(.*?)```"

    # fix aligns
    alignpattern = r"\\begin{align}(.*?)\\end{align}"
    alignreplacement = r"\\begin{align*}\1\\end{align*}"
    gatherpattern = r"\\begin{gather}(.*?)\\end{gather}"
    gatherreplacement = r"\\begin{gather*}\1\\end{gather*}"

    text = re.sub(alignpattern, alignreplacement, text, flags=re.DOTALL)
    text = re.sub(gatherpattern, gatherreplacement, text, flags=re.DOTALL)
    return re.sub(
        tikzpattern,
        createtikzdiagram,
        text,
        flags=re.DOTALL,
    )


def handlefile(src, dst):
    _, ext = os.path.splitext(src)
    if ext == ".md":
        with open(src, "r", encoding="utf-8") as f:
            text = f.read()
            with open(dst, "w", encoding="utf-8") as g:
                g.write(applytransform(text))

        # remove CRLF line endings
        with open(dst, "rb") as f:
            content = f.read()
            content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
        with open(dst, "wb") as f:
            f.write(content)
    else:
        shutil.copy2(src, dst)


def replforpub(src, dst):
    for path in os.listdir(src):
        fullpath = os.path.join(src, path)
        repli = os.path.join(dst, path)
        if os.path.isdir(fullpath):
            os.makedirs(repli)
            replforpub(fullpath, repli)
        elif os.path.isfile(fullpath):
            handlefile(fullpath, repli)


if __name__ == "__main__":

    roots = getroots()
    print(roots)
    if not (roots and checkvalid(roots)):
        print("improper .publish file")
        sys.exit()
    if os.path.isdir(PUBLISH_FOLDER):
        shutil.rmtree(PUBLISH_FOLDER)
    os.makedirs(PUBLISH_FOLDER)
    os.makedirs(f"{PUBLISH_FOLDER}/SVG")
    shutil.copy2("index.md", f"{PUBLISH_FOLDER}/index.md")
    for root in roots:
        repldst = f"{PUBLISH_FOLDER}/{root}"
        os.makedirs(repldst)
        replforpub(root, repldst)
    with open(TIKZ_JSON, "w", encoding="utf-8") as f:
        json.dump(tikzdiagrams, f)

    # Add dependencies
    for dep, exts in DEPENDENCIES.items():
        depdir = os.path.join(PUBLISH_FOLDER, dep)
        os.makedirs(depdir)
        for path in os.listdir(dep):
            fullpath = os.path.join(dep, path)
            replpath = os.path.join(depdir, path)
            if os.path.isfile(fullpath) and os.path.splitext(path)[1] in exts:
                shutil.copy2(fullpath, replpath)

    # Move the files to the public vault
    # contentsfolder = os.path.join(PUBVAULT, "content")
    # shutil.rmtree(contentsfolder)
    # shutil.copytree(PUBLISH_FOLDER, contentsfolder)
    os.chdir(ROOT)
    os.system("npx quartz sync")
