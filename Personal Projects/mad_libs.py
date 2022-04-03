import string

# removes punctuation and splits the string into a list
def punc(grammarList):
    grammarList = grammarList.translate(str.maketrans(" ", " ", string.punctuation))
    grammarList = grammarList.split(" ")
    return grammarList

# prompts user for words
# checks to make sure that the list is specific length
def make_list(grammarType, count):
    grammarList = ""
    while len(grammarList) != count:
        grammarList = punc(input(f"Please enter {count} {grammarType}: "))
    return grammarList

# asks user for the adjectives
adjList = make_list("adjectives", 4)

# asks user for the nouns
nounList = make_list("nouns", 3)

# asks user for the verbs
verbList = make_list("verbs", 3)

#asks users for the adverbs
advList = make_list("adverbs", 2)

print(f"""Today I went to the zoo. I saw a(n) {adjList[0]} {nounList[0]} jumping up and down in its tree. 
He {verbList[0]} {advList[0]} through the large tunnel that led to its {adjList[1]} {nounList[1]}. I got some 
peanuts and passed them through the cage to a gigantic gray {nounList[2]} towering above my head. 
Feeding that animal made me hungry. I went to get a {adjList[2]} scoop of ice cream. It filled my stomach. 
Afterwards I had to {verbList[1]} {advList[1]} to catch our bus. When I got home I {verbList[2]} my mom 
for a {adjList[3]} day at the zoo.""")