import os

file_path = "requirement.txt"

if os.path.exists(file_path):
    print("File Exists")
else:
    print("file not exists")