---
trigger: manual
description: Style guide for creating notes, based on existing markdown files in Class Notes.
---

# Style Guide for Class Notes

This guide outlines the formatting and structural conventions for creating and maintaining class notes, based on the actual usage across the `Class Notes` folder (e.g., `Algebraic Geometry.md`, `Function Spaces.md`, `Optimization.md`, and `Complex analysis.md`).

## 1. Frontmatter

All notes should begin with YAML frontmatter. The minimum requirement is the `publish` flag. Other metadata can be included as needed.

```yaml
---
title: Title of Note
tags:
  - tag1
created: YYYY-MM-DD
publish: true
---
```

## 2. Headings & Structure

- **Title**: Use a single H1 (`#`) for the document title or main topic.
- **Sections**: Use H2 (`##`) for major sections (e.g., "Holomorphic Functions", "Nullstellensatz").
- **Subsections**: Use H3 (`###`) and H4 (`####`) for nested content.
- **Lists**: Use ONLY numbered lists (`1.`, `2.`) for all list items. Do not use bullet points or unordered lists.
- **Dividers**: Use horizontal rules (`---`) to separate distinct topics, proofs, or examples.

## 3. Mathematical Environments (Theorems, Proofs, Definitions)

There are two accepted styles in the notes. The **Bold Text Style** is the most widely used across subjects (Algebra, Topology, Analysis). The **Callout Style** is primarily used in specific notes (e.g., Optimization).

### Option A: Bold Text Style (Preferred & Most Common)

Use bold text for the environment name, followed by a colon or period.

- **Theorems, Lemmas, Propositions**: `**Theorem:**`, `**Lemma:**`, `**Proposition:**`. You can optionally include names, e.g., `**Theorem (Mordell-Weil).**`
- **Definitions**: `**Def:**`, `**Def:(Term)**`, or `**Definition:**`
- **Proofs**: `**Proof:**` or `**Proof Sketch:**`. Conclude with a QED symbol (`$\blacksquare$`).
- **Examples/Exercises**: `**Example:**`, `**Eg:**`, `**Exercise:**`

### Option B: Callout Style (Obsidian/GitHub Style)

Use specific callout types if a more stylized, boxed look is desired.

- **Definitions**: `> [!INFO] Definition:`
- **Theorems/Lemmas/Propositions**: `> [!TIP] Theorem:`
- **Proofs**: `> [!NOTE]- Proof` (collapsible)
- **Examples**: `> [!EXAMPLE]`
- **Questions/Exercises**: `> [!QUESTION]`

## 4. Mathematics (LaTeX)

- **Inline Math**: Use single dollar signs, e.g., `$f(x) = x^2$`.
- **Block Math**: Use double dollar signs, e.g., `$$ f(x) = \int x dx $$`.
- **Environments**:
  - Use `pmatrix` or `bmatrix` for matrices.
  - Use `align`, `align*`, or `gather` for multi-line equations inside `$$` blocks.
- **Common Notation**:
  - Vectors: `\vec{x}`
  - Inner Products: `\langle \vec{x}, \vec{y} \rangle`
  - Norms and absolute values: `|x|`, `\lvert x \rvert`, `||x||`
  - Sets and Spaces: `\mathbb{R}^n`, `\mathbb{C}`, `\mathbb{A}^n`, `\mathcal{V}`
- **Package Dependencies**: Assume standard MathJax/KaTeX support (which Obsidian handles natively).

## 5. Figures & Diagrams

### TikZ Blocks

When generating TikZ figures directly in markdown, follow this code block structure:

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth]
    % TikZ code
\end{tikzpicture}
\end{document}
```

- **Commutative Diagrams**: Use `\usepackage{tikz-cd}` before the `\begin{document}` and `\begin{tikzcd}` instead of `tikzpicture`.
- **Scale**: Keep `scale` at 1.0 or below.
- **Colors & Styling**: Ensure high contrast. Standard colors like `blue!10` for fills and `dashed` for boundaries are common.

### Embedded Images

Use standard Obsidian embedding for hand-drawn figures or external images:

- `![[Drawing 2025-07-21.excalidraw.svg]]` or `![[image.png]]`

## 6. General Formatting

- **Emphasis**: Use `**text**` for emphasis on defined terms or key concepts within a paragraph. Use `*text*` sparingly for lighter emphasis.
- **Links**: Use `[[wikilinks]]` for internal references to other notes.
