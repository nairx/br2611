from pathlib import Path 

# path = Path("students2.txt")
# print(path.exists())
# print(path.is_file())

# folder = Path("reports")
# folder.mkdir(exist_ok=True)

from pathlib import Path 
file = Path('reports/report.txt')
# file.write_text("Sales Report")

data = file.read_text()
print(data)