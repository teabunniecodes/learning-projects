# build a program that takes as input the name of a file. \
# That file will simply contain two lines. Each line is a comma \
# separated list of sorted numbers. Your program should read the \
# file, read in each line as a separate linked list, merge the \
# two lists together, then print the output.

# Personal Projects/Text Files/number_list.txt
# Python/Self Projects/Text Files/number_list.txt 
file = input("Path of text file: ")

with open(file) as read:
    contents = read.read()
    print(contents)
    original = contents.split("\n")
    read.close()

print(original)
length = len(original)

x = 0
y = 0
z = 1
list_ = {}

for int in original:
    list = original[x]
    split_list = list.split(", ")
    if y < length:
        y += 1
        list_[y] = split_list
        print(f"list_{y}: {list_[y]}")
    x += 1
    #print(split_list)

while z < length:
    merge_list = list_[z]
    z += 1
    merge_list = merge_list + list_[z]
    print(f"Merged List: {merge_list}")

# Need to still change the list of strings to int before sort.

merge_list.sort()
print(f"Sorted list: {merge_list}")
