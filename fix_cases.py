import os

cases_dir = r"c:\Users\Bruno Bogochvol\OneDrive\Documentos\GitHub\Singular\portfolio\cases"

for root, dirs, files in os.walk(cases_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if not content.startswith("---"):
                # Extract title
                lines = content.split('\n')
                title = "Case Study"
                for line in lines:
                    if line.startswith("# "):
                        title = line[2:].strip().replace('"', '\\"')
                        break
                
                # Create front matter
                front_matter = f"---\nlayout: default\ntitle: \"{title}\"\n---\n\n"
                
                new_content = front_matter + content
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {file}")
            else:
                print(f"Skipped {file} (already has front matter)")
