# Personal Projects/Text Files/number_list.txt
# Python/Self Projects/Text Files/number_list.txt 

file = input("Path of text file: ")

# opens the txt file and reads and prints out each line
with open(file) as read:
    contents = read.read()
    print(contents)
    # turns each line into a string and puts them together in a list
    original = contents.split("\n")
    read.close()

print(original)
length = len(original)

y = 0
list_ = {}
merge_list = []

# splits each string into single char and then assigns each one a variable name dynamically
for strings in original:
    split_list = strings.split(", ")
    y += 1
    list_[y] = split_list
    print(f"list_{y}: {list_[y]}")

# adds all the lists into one large list
i = length
while i > 0:
    merge_list += list_[i]
    i -= 1

# prints the complete list
print(f"Merged List: {merge_list}")

# changes the strings to int
merge_list = list(map(int, merge_list))
print(f"Int List: {merge_list}")

# sorts all the ints in ascending order
merge_list.sort()
print(f"Sorted list: {merge_list}")
