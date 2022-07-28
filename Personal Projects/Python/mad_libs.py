import string

adjList = []
nounList = []
verbList = []
advList = []

def punc(grammar):
    # remove any punctuation the user may have inputted
    grammar = grammar.translate(str.maketrans(" ", " ", string.punctuation))
    grammar = grammar.split(" ")
    return grammar

def getList(length, punctuation):
    puncList = []
    while len(puncList) != length:
        puncList = punc(input(f"Please enter {length} {punctuation}s: "))
    return puncList

adjList = getList(4, "adjective")
nounList = getList(3, "noun")
verbList = getList(3, "verb")
advList = getList(2, "adverb")

print(f"""Today I went to the zoo. I saw a(n) {adjList[0]} {nounList[0]} jumping up and down in its tree. 
He {verbList[0]} {advList[0]} through the large tunnel that led to its {adjList[1]} {nounList[1]}. I got some 
peanuts and passed them through the cage to a gigantic gray {nounList[2]} towering above my head. 
Feeding that animal made me hungry. I went to get a {adjList[2]} scoop of ice cream. It filled my stomach. 
Afterwards I had to {verbList[1]} {advList[1]} to catch our bus. When I got home I {verbList[2]} my mom 
for a {adjList[3]} day at the zoo.""")

# first line = list
# second line = loop to check there are correct number of arguments inputted
# third line = asking the user for the specific amount of arguments needed in the list