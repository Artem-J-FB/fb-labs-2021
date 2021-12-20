import sys  # arguments
import math # logarithm

ruDict = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def sortDict(rawDict):
    sortedDict = {}
    for i in sorted(rawDict):
        sortedDict[i]=rawDict[i]
    return sortedDict

def flipSortDict(rawDict):
    sortedDict = {}
    invDict = {v: k for k, v in rawDict.items()}
    for i in sorted(invDict, reverse=True):
        sortedDict[i]=invDict[i]
    return {v: k for k, v in sortedDict.items()}

if len(sys.argv) < 2:
    print("Usage: topBiFreq.py <source file>")
    exit(0)

f = open(sys.argv[1])
f.seek(0)
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

for bi in biFreq:
    biFreq[bi] = biFreq[bi]/totalBiChars

biFreq = flipSortDict(biFreq)
i = 0
for bf in biFreq:
    if i == 5:
        break
    print(bf, biFreq[bf])
    i += 1
    
