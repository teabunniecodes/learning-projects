# prompt the user for a number
height = int(input("Please choose an integer between 1-8: "))
# limit the input between 1-8
while height < 0 or height > 8:
    height = int(input("Please choose an integer between 1-8: "))
for brick in range(height):
    brick += 1
    line = (height * str(" ")) + (brick * str("#"))
    height -= 1
print(line)