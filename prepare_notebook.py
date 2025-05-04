import nbformat
import os
import subprocess

notebook = "sirs_interactive_page.ipynb"

# Load and modify notebook metadata
with open(notebook, "r") as f:
    nb = nbformat.read(f, as_version=4)

nb.metadata.kernelspec = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
}
nb.metadata.language_info = {
    "name": "python"
}

# Optionally clear outputs
for cell in nb.cells:
    if "outputs" in cell:
        cell["outputs"] = []
    if "execution_count" in cell:
        cell["execution_count"] = None

with open(notebook, "w") as f:
    nbformat.write(nb, f)

# Trust the notebook
subprocess.run(["jupyter", "trust", notebook])

print("✅ Notebook trusted, metadata set, and outputs cleared.")

