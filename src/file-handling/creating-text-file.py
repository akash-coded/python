try:
    with open('src/file-handling/sample-files/new-file.txt', 'x') as f:
        f.write('Create a new text file in Python')
except FileExistsError:
    print("The given file already exists")
