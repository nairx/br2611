from glob import glob 
from pathlib import Path

# files = glob("*.py")
# print(files)


# files = glob("01_python_fundamentals/*.py")
# # print(files)
# for file in files:
#     print(file)


folder = Path(".")
for file in folder.rglob("*.py"):
    with open(file,'r') as f:
        data = f.read()
        if "John" in data:
            print(file)