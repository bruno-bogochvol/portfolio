import os

cases_dir = r"c:\Users\Bruno Bogochvol\OneDrive\Documentos\GitHub\Singular\portfolio\cases"

for root, dirs, files in os.walk(cases_dir):
    for file in files:
        if file == "README.md" and root != cases_dir:
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, "index.md")
            os.rename(old_path, new_path)
            print(f"Renamed {old_path} to {new_path}")
