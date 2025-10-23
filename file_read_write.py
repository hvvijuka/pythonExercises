""" open("test.txt", "r") as f:
content = f.read()      
print("File content:\n", content)
#f.write("This is a test file.\nIt contains multiple lines.\nThis is the third line.") """

import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')

with open("test1.txt", "w") as fp:
    str1 = "line1.\nline2.\nline3.\nline4.\nline5.\n"
    fp.write(str1)

with open("test1.txt", "r") as fp:
    
    content = fp.readlines()
    count = 0
    for lines in content:
        
        count += 1
        if count ==4 :
            print("File content:\n", lines)

# read test.txt
#with open("test.txt", "r") as fp:
#    # read all lines from a file
#    lines = fp.readlines()
#    print("File content:", lines)

# open new file in write mode
#with open("new_file.txt", "w") as fp:
#    count = 0
#    # iterate each lines from a test.txt
#    for line in lines:
#        # skip 5th lines
#        if count == 4:
#            count += 1
#            continue
#        else:
#            # write current line
#            fp.write(line)
#        # in each iteration reduce the count
#        count += 1
#
##copy two files
#with open("test.txt", "r") as source_file:
#    with open("copied_file.txt", "w") as dest_file:
#        for line in source_file:
#            dest_file.write(line)           
#
#
##xonxvert file content to uppercase and write to new file
#with open("test.txt", "r") as source_file:
#    with open("uppercase_file.txt", "w") as dest_file:
#        for line in source_file:
#            dest_file.write(line.upper()) 
#
#
##concatenate two files
#with open("test.txt", "r") as file1, open("new_file.txt", "r") as file2:
#    with open("concatenated_file.txt", "w") as dest_file:
#        for line in file1:
#            dest_file.write(line.upper())
#        for line in file2:
#            dest_file.write(line)   