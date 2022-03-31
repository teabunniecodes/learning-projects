# build a program that takes as input the name of a file. \
# That file will simply contain two lines. Each line is a comma \
# separated list of sorted numbers. Your program should read the \
# file, read in each line as a separate linked list, merge the \
# two lists together, then print the output.



# file path - Personal Projects/Text Files/number_list.txt
file = input("Path of text file: ")

with open(file) as read:
    contents = read.read()
    print(contents)
    original = contents.split("\n")
    read.close()

print(original)

x = 0
for int in original:
    list = original[x]
    print(list.split())
    x +=1
    #combined = original[x-1] - original [x]

print()
