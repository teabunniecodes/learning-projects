# prompt user for height of the steps
height = int(input("Please enter an integer between 1-8: "))
# limit input of height between 1-8
# prompt user to re-enter a number if outside the parameters
while height < 0 or height > 8:
    height = int(input("Please enter an integer between 1-8: "))
# if user inputs a number between 1-8 
for brick in range(height):
    brick += 1
    line = (height * str(" ")) + (brick * str("#")) + (" ") + (brick * str("#"))
    height -= 1
    print(line)