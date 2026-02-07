import xml.etree.ElementTree as ET
import re
import sys

# Force utf-8 for stdout if possible, or just ignore errors
sys.stdout.reconfigure(encoding='utf-8')

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

try:
    tree = ET.parse(r'c:\Users\shameel\Documents\Notes\content\Class Notes\temp_extract\extracted\word\document.xml')
    root = tree.getroot()
    
    body = root.find('w:body', ns)
    
    current_chapter = "Preamble"
    content = {current_chapter: []}
    order = [current_chapter]
    
    # Improved Regex for Chapter/Section detection
    # Captures: "Chapter 1", "1. Section", "§1", "I. Part", etc.
    # The source might use "1 Plane curves" type headings.
    
    for p in body.findall('w:p', ns):
        texts = p.findall('.//w:t', ns)
        para_text = ''.join([t.text for t in texts if t.text])
        
        if not para_text.strip():
            continue
            
        # Check for Heading
        # Matches: "Chapter 1", "1 Plane curves", "2 Affine algebraic sets"
        # Be careful not to match "1.1 definition" if we only want chapters.
        # Let's try to capture "Chapter X" or single digits at start of line followed by text.
        
        # Heuristic: <w:pStyle w:val="Heading1"/> usually denotes chapters.
        # But we don't have style info easily accessible without more XML parsing.
        # We'll stick to text heuristics.
        
        is_heading = False
        if re.match(r'^\s*(Chapter\s+\d+|[1-9]\s+[A-Z][a-zA-Z\s]+)$', para_text.strip()):
            is_heading = True
        elif re.match(r'^\s*Part\s+[IVX]+', para_text.strip()):
            is_heading = True

        if is_heading and len(para_text) < 100:
             current_chapter = para_text.strip()
             if current_chapter not in content:
                 content[current_chapter] = []
                 order.append(current_chapter)
        
        content[current_chapter].append(para_text)

    # Output to files
    for chap in order:
        safe_name = re.sub(r'[^a-zA-Z0-9]', '_', chap)
        filename = f"extracted_{safe_name}.txt"
        print(f"Writing {filename}...")
        with open(filename, "w", encoding="utf-8") as f:
            f.write('\n\n'.join(content[chap]))

except Exception as e:
    print(f"Error: {e}")
