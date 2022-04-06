# takes text input from the user
text = input("Please enter text: ")
# find the amount of letters in the text
x = 0
letters = 0
for alphabet in text:
    atoi_text = ord(alphabet[x])
    if (atoi_text >= ord("A") and atoi_text <= ord("Z")) or (atoi_text >= ord("a") and atoi_text <= ord("z")):
        letters += 1
print(f"Letters: {letters}")
# find the amount of words in the text
words = text.count(" ") + 1
print(f"Words: {words}")
# find the amount of sentences in the text
sentences = text.count(".") + text.count("!") + text.count("?")
print(f"Sentences: {sentences}")
# find the average amount of letters per 100 words
avg_letters = float(letters / words * 100)
print(avg_letters)
# find the average amount of sentences per 100 words
avg_sentences = sentences / words * 100
# calculate the grade level of the reading material
grade = (0.0588 * avg_letters) -  (0.296 * avg_sentences) - 15.8
print(grade)
# tells the user what grade level the text is
if grade >= 1 and grade < 16:
    print(f"Grade: {round(grade)}")
# if the grade is less than 1 "Before Grade 1"
if grade < 1:
    print(f"Grade: Before Grade 1")
# if the grade is greater than 16 "Grade 16+"
if grade >= 16:
    print(f"Grade: 16+")