import os

root_dir = r"c:\Users\Bruno Bogochvol\OneDrive\Documentos\GitHub\Singular\portfolio"
for root, dirs, files in os.walk(root_dir):
    if ".git" in dirs:
        dirs.remove(".git")
    for file in files:
        if file.endswith((".md", ".html", ".yml", ".py")):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                if "README.md" in content:
                    print(f"Found in {path}")
