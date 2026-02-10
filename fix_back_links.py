import os
import re

cases_dir = r"c:\Users\Bruno Bogochvol\OneDrive\Documentos\GitHub\Singular\portfolio\cases"

def update_file(path, pattern, replacement):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = re.sub(pattern, replacement, content)
    
    if content != new_content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {path}")

for root, dirs, files in os.walk(cases_dir):
    for file in files:
        path = os.path.join(root, file)
        
        # Update index.md: ../../README.md -> ../../
        if file == "index.md":
            update_file(path, r"\.\./\.\./README\.md\)", "../../)")
            
        # Update README_EN.md: ../../README_EN.md -> ../../README_EN.html
        elif file == "README_EN.md":
            update_file(path, r"\.\./\.\./README_EN\.md\)", "../../README_EN.html)")
