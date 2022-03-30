# build a program that takes as input the name of a file. \
# That file will simply contain two lines. Each line is a comma \
# separated list of sorted numbers. Your program should read the \
# file, read in each line as a separate linked list, merge the \
# two lists together, then print the output.

list_1 = []
list_2 = []

file = input("Path of text file: ")

with open(file) as file:
    contents = file.readlines()
    print(contents)
    file.close()

count = 0
for lists in contents:
    count += 1
    print(f"list {count}: {lists}")
    list_1 = lists.split(",")
    list_2 = lists.split(",")

print(list_1)
print(list_2)
