try:
    f = open('src/file-handling/sample-files/demo-file-1.txt')
    # perform file operations
    contents = f.read()
finally:
    f.close()
print(contents)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

with open('src/file-handling/sample-files/demo-file-1.txt') as f:
    # perform file operations
    lines = f.readlines()
print(lines)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


with open('src/file-handling/sample-files/demo-file-1.txt') as f:
    [print(line.strip()) for line in f.readlines()]
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
