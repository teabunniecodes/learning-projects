import string

def punc(grammar):
    grammar = grammar.translate(str.maketrans(" ", " ", string.punctuation))
    grammar = grammar.split(" ")
    return grammar

# mad libs beginner python project
adjList = []
while len(adjList) != 4:
    adjList = punc(input("Please enter 4 adjectives: "))

nounList = []
while len(nounList) != 3:
    nounList = punc(input("Please enter 3 nouns: "))

verbList = []
while len(verbList) != 3:
    verbList = punc(input("Please enter 3 verbs: "))

advList = []
while len(advList) != 2:
    advList = punc(input("Please enter 2 adverbs: "))

print(f"""Today I went to the zoo. I saw a(n) {adjList[0]} {nounList[0]} jumping up and down in its tree. 
He {verbList[0]} {advList[0]} through the large tunnel that led to its {adjList[1]} {nounList[1]}. I got some 
peanuts and passed them through the cage to a gigantic gray {nounList[2]} towering above my head. 
Feeding that animal made me hungry. I went to get a {adjList[2]} scoop of ice cream. It filled my stomach. 
Afterwards I had to {verbList[1]} {advList[1]} to catch our bus. When I got home I {verbList[2]} my mom 
for a {adjList[3]} day at the zoo.""")