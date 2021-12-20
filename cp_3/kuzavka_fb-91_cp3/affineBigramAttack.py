import sys
import math

ruDict31 = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
M = 31 # size of the alphabet
MAX = 500 # maximum value of the a and b
FORBIDDEN_BIGRAMS = ['яь', 'ыь', 'оь', 'шя']
#FORBIDDEN_BIGRAMS = ['аы', 'аь', 'бй', 'бф', 'вй', 'гй', 'гц', 'гщ', 'гы', 'гю', 'дй', 'еы', 'еь', 'жй', 'жф', 'жх', 'жщ', 'жы', 'жю', 'зй', 'зщ', 'иы', 'иь', 'йй', 'йы', 'йь', 'кй', 'кы', 'кь', 'лй', 'мй', 'нй', 'оы', 'оь', 'пв', 'пг', 'пй', 'пх', 'пщ', 'пэ', 'рй', 'сй', 'тй', 'уы', 'уь', 'фд', 'фж', 'фз', 'фй', 'фм', 'фп', 'фх', 'фц', 'фш', 'фщ', 'фэ', 'хй', 'хы', 'хь', 'цй', 'цф', 'цч', 'цщ', 'ць', 'цэ', 'цю', 'чй', 'чф', 'чщ', 'чы', 'чю', 'шз', 'шй', 'шф', 'шщ', 'шы', 'шэ', 'шя', 'щб', 'щг', 'щд', 'щж', 'щз', 'щй', 'щк', 'щм', 'щс', 'щт', 'щф', 'щх', 'щц', 'щч', 'щш', 'щщ', 'щы', 'щэ', 'щю', 'щя', 'ыы', 'ыь', 'ыю', 'ьй', 'ьы', 'ьь', 'эа', 'эб', 'эв', 'эе', 'эж', 'эм', 'эо', 'эу', 'эф', 'эх', 'эц', 'эч', 'эщ', 'эы', 'эь', 'ээ', 'эю', 'эя', 'юй', 'юы', 'юь', 'яы', 'яь']

cipherText = open(sys.argv[1], 'r')
CTmostFreq = ['сг', 'жэ', 'ям', 'нг', 'тм']

def affineBiDecode(cipherText, inv_a, b):
    cipherText.seek(0)
    plainText = ''
    for string in cipherText:
        for i in range(0, len(string) - 1, 2):
            biGramCT = string[i:i+2]
            biGramCTnum = ruDict31.index(biGramCT[0])*M + ruDict31.index(biGramCT[1])
            biGramPTnum = ((biGramCTnum - b)*inv_a) % (M*M)
            plainText += ruDict31[int((biGramPTnum - (biGramPTnum % M))/M)]
            plainText += ruDict31[biGramPTnum % M]
    return plainText

def forbiddenBiGramsFilter(text):
    for fBiGram in FORBIDDEN_BIGRAMS:
        if fBiGram in text:
            return True
    return False

def flipSortDict(rawDict):
    sortedDict = {}
    invDict = {v: k for k, v in rawDict.items()}
    for i in sorted(invDict, reverse=True):
        sortedDict[i]=invDict[i]
    return {v: k for k, v in sortedDict.items()}

def mostFreqLetterFilter(text):
    freq={}
    for string in text:
        for i in string:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    freq = flipSortDict(freq)
    mostFreq = ''
    for letter in freq:
        mostFreq = letter
        break
    if mostFreq == 'о':
        return False
    else:
        return True

q = 0
for c in CTmostFreq:
    bigramCTnum = ruDict31.index(c[0])*M + ruDict31.index(c[1])
    for a in range(0, MAX):
        if math.gcd(a, M) != 1:
            continue
        inv_a = pow(a, -1, M*M)
        for b in range (0, MAX):
            if ((bigramCTnum - b)*inv_a) % (M*M) != 572: # Найчастіша біграма - "то".
                continue
            plainText = affineBiDecode(cipherText, inv_a, b)
            if mostFreqLetterFilter(plainText) or forbiddenBiGramsFilter(plainText):
                continue
            else:
                q += 1
                print(plainText)
                print('a =', a, '; b =', b, end='\n\n')
