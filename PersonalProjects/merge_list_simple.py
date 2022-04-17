# Personal Projects/Text Files/number_list.txt
# Python/Self Projects/Text Files/number_list.txt 

file = input("Path of text file: ")

with open(file) as read:
    contents = read.read()
    print(contents)
    original = contents.split("\n")
    read.close()

print(original)

# split out each string into separate lists
lists = [line.split(", ") for line in original]
print(lists)
# flatten the list inside of lists
flattenedList = sum(lists, [])
# convert list of strings into list of ints
numberedList = list(map(int, flattenedList))
# sort
numberedList.sort()
print(numberedList)