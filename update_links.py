import re

readme_path = r"c:\Users\Bruno Bogochvol\OneDrive\Documentos\GitHub\Singular\portfolio\README.md"
readme_en_path = r"c:\Users\Bruno Bogochvol\OneDrive\Documentos\GitHub\Singular\portfolio\README_EN.md"

def update_file(path, pattern, replacement):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Debug print to ensure we are matching
    matches = re.findall(pattern, content)
    print(f"Found {len(matches)} matches in {path}")

    new_content = re.sub(pattern, replacement, content)
    
    if content != new_content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {path}")
    else:
        print(f"No changes needed for {path}")

# Update README.md: /README.md) -> /)
# Matches things like [View case]({{ site.baseurl }}/cases/nubo-educacao/README.md)
update_file(readme_path, r"/README\.md\)", "/)")

# Update README_EN.md: /README_EN.md) -> /README_EN.html)
# Matches things like [View case]({{ site.baseurl }}/cases/nubo-educacao/README_EN.md)
update_file(readme_en_path, r"/README_EN\.md\)", "/README_EN.html)")
