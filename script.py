import nbformat
from nbclient import NotebookClient

# Load the notebook
notebook_path = "main.ipynb"
with open(notebook_path) as f:
    nb = nbformat.read(f, as_version=4)

# Create a Notebook Client
client = NotebookClient(nb, timeout=600, kernel_name='python3')

# Start the kernel and execute the notebook (all cells)
client.execute()

# Define the specific cell indices to execute: (1-3), (6-7), (9-10)
cells_to_run = list(range(1, 4)) + list(range(6, 8)) + list(range(9, 11))

# Execute the selected cells
for i in cells_to_run:
    try:
        client.execute_cell(nb.cells[i], i)
    except Exception as e:
        print(f"Error executing cell {i}: {e}")

# Save the executed notebook
output_path = "executed_notebook_case_custom.ipynb"
with open(output_path, "w") as f:
    nbformat.write(nb, f)

print(f"Notebook executed and saved as {output_path}")