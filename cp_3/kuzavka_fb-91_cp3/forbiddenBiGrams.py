import sys  # arguments
ruDict = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']

def sortDict(rawDict):
    sortedDict = {}
    for i in sorted(rawDict):
        sortedDict[i]=rawDict[i]
    return sortedDict

if len(sys.argv) < 2:
    print("Usage: forbiddenBiGrams.py <source file>")
    exit(0)

f = open(sys.argv[1])
biFreq = {}
for string in f:
    for i in range(0, len(string) - 1, 2): # ..., 2) to count bigrams with 2 char step.
        biGram = string[i:i+2]
        if biGram in biFreq:
            biFreq[biGram] += 1
        else:
            biFreq[biGram] = 1

totalBiChars = 0                           # Same as totalChars - 1 (for step = 1).
for bi in biFreq:
    totalBiChars += biFreq[bi]

# Now we have the pairs "char - how many times it was in the text".
# Let's calculate the frequency.

for bi in biFreq:
    biFreq[bi] = biFreq[bi]/totalBiChars

biFreq = sortDict(biFreq)
for letter1 in ruDict:
    for letter2 in ruDict:
        bi = letter1+letter2
        if bi not in biFreq:
            print('\'', bi, '\'', ', ', sep='', end='')

print()


