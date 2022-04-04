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

y = 0
list_ = {}
merge_list = []

for strings in original:
    split_list = strings.split(", ")
    y += 1
    list_[y] = split_list
    print(f"list_{y}: {list_[y]}")

i = length
while i > 0:
    merge_list += list_[i]
    i -= 1

print(f"Merged List: {merge_list}")

merge_list = list(map(int, merge_list))
print(f"Int List: {merge_list}")

merge_list.sort()
print(f"Sorted list: {merge_list}")