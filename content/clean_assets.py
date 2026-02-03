
import os
import re
import shutil
import urllib.parse

# Configuration
CONTENT_DIR = "."  # Root content directory
ASSETS_DIR = "Assets"
TRASH_DIR = os.path.join(ASSETS_DIR, "_trash")

# Extensions to consider as assets
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp'}

def get_all_assets(assets_dir):
    """Recursively find all image files in the assets directory."""
    assets = set()
    if not os.path.exists(assets_dir):
        return assets
    
    for root, dirs, files in os.walk(assets_dir):
        if "_trash" in root: # Skip trash
            continue
            
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                # We store just the filename because Obsidian wiki-links usually just use filename
                # If there are duplicates in subfolders, this simple approach considers them "the same" reference
                # which is safer (won't delete if referenced).
                assets.add(file)
    return assets

def get_referenced_images(content_dir):
    """Scan all markdown files for image references."""
    referenced = set()
    
    # Regex for [[image.png]] or [[image.png|alt]]
    wiki_link_pattern = re.compile(r'\[\[(.*?)(?:\|.*?)?\]\]')
    
    # Regex for ![alt](image.png) or [alt](image.png)
    # This also captures standard links
    md_link_pattern = re.compile(r'\[.*?\]\((.*?)\)')

    for root, dirs, files in os.walk(content_dir):
        if ".obsidian" in root or "_trash" in root:
            continue
            
        for file in files:
            if file.endswith(".md") or file.endswith(".canvas"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Find wiki links
                        for match in wiki_link_pattern.findall(content):
                            # Clean up the match (sometimes has path/to/image.png)
                            filename = os.path.basename(match)
                            referenced.add(filename)
                            # Also add the raw match in case it's path based
                            referenced.add(match)

                        # Find markdown links
                        for match in md_link_pattern.findall(content):
                            # Unquote URL (e.g. %20 -> space)
                            url = urllib.parse.unquote(match)
                            filename = os.path.basename(url)
                            referenced.add(filename)
                            referenced.add(url)
                            
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    
    return referenced

def clean_assets():
    print(f"Scanning for assets in: {ASSETS_DIR}")
    all_assets = get_all_assets(ASSETS_DIR)
    print(f"Found {len(all_assets)} total asset files.")
    
    print(f"Scanning for references in: {CONTENT_DIR}")
    referenced_assets = get_referenced_images(CONTENT_DIR)
    print(f"Found {len(referenced_assets)} unique references found in notes.")
    
    # Identify unused
    # We check if asset filename appears in references
    # Note: This is an approximation. If you have "image.png" in assets and "Folder/image.png" in link,
    # os.path.basename handles it.
    
    unused_assets = []
    
    for asset in all_assets:
        if asset not in referenced_assets:
            # Double check URL encoded version just in case
            encoded = urllib.parse.quote(asset)
            if encoded not in referenced_assets:
                 unused_assets.append(asset)
    
    print(f"Found {len(unused_assets)} unused assets.")
    
    if not unused_assets:
        print("No unused assets found. Clean!")
        return

    # Create trash directory
    if not os.path.exists(TRASH_DIR):
        os.makedirs(TRASH_DIR)
        print(f"Created trash directory: {TRASH_DIR}")
    
    # Move unused assets
    print("Moving unused assets to _trash...")
    count = 0
    for asset in unused_assets:
        # Find the full path again to move it (inefficient but safe)
        found = False
        for root, dirs, files in os.walk(ASSETS_DIR):
            if "_trash" in root: continue
            if asset in files:
                 src_path = os.path.join(root, asset)
                 dst_path = os.path.join(TRASH_DIR, asset)
                 
                 # Handle name collision in trash
                 if os.path.exists(dst_path):
                     base, ext = os.path.splitext(asset)
                     import time
                     dst_path = os.path.join(TRASH_DIR, f"{base}_{int(time.time())}{ext}")
                 
                 try:
                    shutil.move(src_path, dst_path)
                    print(f"Moved: {asset}")
                    count += 1
                    found = True
                    break # Move only first occurrence if dupe names exist in different folders (simplification)
                 except Exception as e:
                     print(f"Failed to move {asset}: {e}")
        
    print(f"Successfully moved {count} files to {TRASH_DIR}")

if __name__ == "__main__":
    clean_assets()
