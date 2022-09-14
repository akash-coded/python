import os.path
from pathlib import Path

file_exists = os.path.exists('src/file-handling/sample-files/new-file.txt')
print(file_exists)

file_exists = os.path.exists('src/file-handling/sample-files/new-new-file.txt')
print(file_exists)

path_to_file = 'src/file-handling/sample-files/new-file.txt'
path = Path(path_to_file)

if path.is_file():
    print(f"The file {path_to_file} exists")
else:
    print(f"The file {path_to_file} does not exist")
    