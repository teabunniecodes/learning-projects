# ask user for number to use as the key to the cipher
key = int(input("Please enter an integer greater than 1: "))
# ask user for the text to be translated into cipher text
plain_text = (input("Plain Text: "))
# declare variable for loop to print on 1 line
word = ""
# take the text and convert the characters into ASCII
for letter in plain_text:
    # checks if the character is lower case, upper case, or not a letter
    if letter.islower():
        lower_letter = chr((((ord(letter) - ord("a")) + key) % 26) + ord("a"))
        word += lower_letter
    elif letter.isupper():
        upper_letter = chr((((ord(letter) - ord("A")) + key) % 26) + ord("A"))
        word += upper_letter
    else:
        word += letter
# prints the ciphered text
print(word)