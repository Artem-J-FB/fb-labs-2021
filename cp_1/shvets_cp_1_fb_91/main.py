# -*- coding: utf-8 -*-
import math
import sys
import xlsxwriter
import pandas as pd
import openpyxl
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

#array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","А","Ы","В"]
array = [u"А", u"Б", u"В", u"Г", u"Д", u"Е", u"Ё", u"Ж", u"З", u"И", u"Й", u"К", u"Л", u"М", u"Н", u"О", u"П", u"Р", u"С", u"Т", u"У", u"Ф", "Х", "Ц", u"Ч", u"Ш", u"Щ", u"Ъ", u"Ы", u"Ь", u"Э", u"Ю", u"Я"]

def del_content(text):
    text2 = ""
    text.upper().replace("Ё","Е")
    text.upper().replace("Ъ","Ь")
    print("-----------------------", array)
    for i in range(0, len(text), 1):
        if(array.count(text[i]) == 1 and array.count(text[i].upper()) == 1):
            text2 = text2 + text[i]
    return text2.upper()

def file_content():

    f = open("words.txt", "r", encoding="UTF-8", errors='ignore')
    text_of_the_file = ""
    for lines in f.readlines():
        text_of_the_file = text_of_the_file + lines




    f.close()

    return del_content(text_of_the_file.upper())

array.pop(27)
array.pop(6)
text = file_content().upper()
def frequency(text, letter):
    return int(text.count(letter))/int(len(text)) #return the frequency of a single letter

def frequency_bigram(text, string, amount_of_bigrams):
    return text.count(string)/int(amount_of_bigrams)


bigrams = []
bigrams_frequency = []
all_bigrams = []
def frequency_of_all_bigrams(text):

    if(int((len(text)%2)) != int(0)):
        text = text + " "
    amount_of_bigrams = int(len(text)) - 1
    for x in range(len(array)):

        for i in range(len(array)):
            string = array[x] + array[i]
            fr = frequency_bigram(text, string,  amount_of_bigrams)
            bigrams.append((string, fr))
            bigrams_frequency.append(fr)






ubigrams = []
unique_bigrams = []
ubigrams_frequency = []
def frequency_of_unique_bigram(text):
    if(len(text)%2 != 0):
        text = text + "А"
    amount_of_bigrams = len(text)
    print(" --- ", len(text))
    for x in range(len(array)):
        for i in range(len(array)):
            string = array[x] + array[i]
            unique_bigrams.append(string)
    for i in range(0, len(text),2):
        string = text[i] + text[i+1]
        ubigrams.append(string)
    for i in range(len(unique_bigrams)):
        fr = ubigrams.count(unique_bigrams[i])/len(ubigrams)
        ubigrams_frequency.append(fr) #devide the amount of an bigram in the pool and the amount of all bigram in the pool


pairs = []
letters_frequency = []
def frequency_letter(text):

    print("The amount of words is: ",len(text))

    for x in range(len(array)):
        fr = frequency(text, array[x]) + frequency(text, array[x].lower())
        pairs.append(( array[x].lower(), fr))
        letters_frequency.append(fr)


    print("-----------------------------------------------------------------------------------------------------------------------------------")
    for row in pairs:
        print(row)

def entropy(text, list, n): #search the entropy

    result = 0
    for i in range(0, len(list), 1):
        if list[i] != 0:
            result = result + (1/n)*list[i]*math.log(1/list[i],2)
    return result
arr = []
def to_excel(mass, array, name):
    b_arr = []
    for k in range(len(array)):
        for i in range(len(mass)):
            if(i%len(array) == 0 and i != 0):
                arr.append(b_arr)
                b_arr = []
            b_arr.append(mass[i])

    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()
    row = 0
    column = 0

    for row in range(len(array)):
        for column in range(len(arr[row])):
            worksheet.write(row+1, column+1, str(arr[row][column]))
    workbook.close()

def letters_to_excel(mass, array, name):
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()
    row = 0
    column = 0
    for row in range(len(array)):
            worksheet.write(row + 1, column + 2, str(mass[row]))
    workbook.close()
print(u'ывавЫ ', len(array))
print("The frequency of all letters\n")
frequency_letter(text)
print(
    "-----------------------------------------------------------------------------------------------------------------------------------")
print("The frequency of all bigrams\n")
frequency_of_all_bigrams(text)
print(
    "-----------------------------------------------------------------------------------------------------------------------------------")
frequency_of_unique_bigram(text)
print(
    "-----------------------------------------------------------------------------------------------------------------------------------")
print("Entropy of letters = ", entropy(text, letters_frequency, 1))
print("Entropy of bigrams = ", entropy(text, bigrams_frequency, 2))
print("Entropy of unique bigrams = ", entropy(text, ubigrams_frequency, 2))
print(
    "-----------------------------------------------------------------------------------------------------------------------------------")

to_excel(bigrams_frequency, array, "bigrams_frequency_no_space.xlsx")
to_excel(ubigrams_frequency, array, "ubigrams_frequency_no_space.xlsx")
letters_to_excel(letters_frequency, array, "letters_frequency_no_space.xlsx")