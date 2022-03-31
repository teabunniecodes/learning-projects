# build a program that takes as input the name of a file. \
# That file will simply contain two lines. Each line is a comma \
# separated list of sorted numbers. Your program should read the \
# file, read in each line as a separate linked list, merge the \
# two lists together, then print the output.



# Personal Projects/Text Files/number_list.txt
file = input("Path of text file: ")

with open(file) as read:
    contents = read.read()
    print(contents)
    original = contents.split("\n")
    read.close()

print(original)

x = 0
y = 1
for int in original:
    list = original[x]
    split_list = list.split(", ")
    list = dict()
    for y in range(len(original)):
        list[y] = split_list
        y += 1
        print(list)
    x += 1
    print(split_list)


