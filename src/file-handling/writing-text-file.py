lines = ['Readme', 'How to write text files in Python', ]

with open('src/file-handling/sample-files/new-file-1.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

with open('src/file-handling/sample-files/new-file-2.txt', 'w') as f:
    f.writelines(lines)

more_lines = ['', 'Append text files in Python', 'The End']
with open('src/file-handling/sample-files/new-file-1.txt', 'a') as f:
    f.write('\n'.join(more_lines))
