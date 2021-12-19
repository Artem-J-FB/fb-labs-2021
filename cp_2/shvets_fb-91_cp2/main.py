# -*- coding: utf-8 -*-
import sys
import math
keys = ["МЫ", "ПЕС", "РЫБА", "МАЗУТ", "ИНДЕКСАЦИЯ"]
array = [u"А", u"Б", u"В", u"Г", u"Д", u"Е", u"Ж", u"З", u"И", u"Й", u"К", u"Л", u"М", u"Н", u"О", u"П", u"Р", u"С", u"Т", u"У", u"Ф", "Х", "Ц", u"Ч", u"Ш", u"Щ", u"Ъ", u"Ы", u"Ь", u"Э", u"Ю", u"Я"]
popular = ["О", "А", "Е", "И", "Н", "Т", "Р", "С", "Л", "В","К","П","М","У","Д","Ч"]
def file_content(name):
    f = open(name, "r", encoding="UTF-8")
    text_of_the_file = ""
    for lines in f.readlines():
        text_of_the_file = text_of_the_file + lines
    f.close()
    return text_of_the_file
def print_text(text):
    print(text)
def del_content(text):
    text2 = ""
    new_text = text.upper().replace("Ё","Е").replace(" ", "").replace("\n","").replace(".","").replace("-","").replace(",","").replace(" ","").replace(":","").replace("!","")

    return new_text
def encryption(text, key):
    index = []
    for letter in key:
        ind = array.index(letter)
        index.append(ind)
    pos = 0
    encrypted_text = ""
    for i in text:
        if(i != '\n'):
            if(pos == len(key)):
                pos = 0
            encrypted_text = encrypted_text + array[(array.index(key[pos]) + array.index(i))%int(32)]
            pos = pos + 1

    return encrypted_text
af_index = []
def Affinity_Index(encrypted_text):
    index = 0
    sum = 0
    for i in array:
        sum = sum + encrypted_text.count(i)
        index += encrypted_text.count(i)*(encrypted_text.count(i) - 1)
    index2 = index/((len(encrypted_text))*(len(encrypted_text) - 1))
    #af_index.append(index2)
    return index2


def encrypt(name):
    text = file_content(name)
    text = del_content(text)
    fn = open(name, "w+", encoding="UTF-8")
    fn.write(text)
    fn.close()
    #print_text(text)
    for key in keys:
        name = "key_" + key + ".txt"
        print("-------------------------------------------------------------------------------------------------------")
        print(name)
        f = open(name, "w+", encoding="UTF-8")
        encrypted_text = encryption(text, key)
        f.write(encrypted_text)
        index = Affinity_Index(encrypted_text)
        f.close()
        print("key - ", key," | length - ", len(key)," | affinity index - ", index)


array_of_sections = []

def devide(text, len_key):
    sections = []
    for i in range(0, len_key):
        sec = []
        while(i < len(text)):
            sec.append(text[i])
            i = i+len_key
        sections.append(sec)
   # for item in sections:
    #    print(item)
    return sections

st_i = []
st_sections = []
def decrypt(sections):
    pair = []
    sum = 0
    for i in sections:
        sum = sum + Affinity_Index(i)
    result = sum/len(sections)
    if(abs(0.0553 - result) < 0.005):
        pair.append(result)
        pair.append(len(sections))
        st_i.append(pair)
        array_of_sections.append(sections)

keys_length = []
def decryption(array_of_sections):
    print("__________________________________________________")
    for i in popular:
        print(i, end=' ')
    print("\n")
    for sections in array_of_sections:
        for sec in sections:
            most_common = 0
            for item in array:
                qty = sec.count(item)
                if (qty > most_common):
                    most_common = qty
                    most_common_letter = item
            for i in popular:
                k = (array.index(most_common_letter) - array.index(i))%len(array)
                print(array[k], end=' ')
            print("__")
def decr(file_to_decrypt):
    f = open(file_to_decrypt, "r", encoding="UTF-8")
    encrypted_text = f.read().upper()
    key = input("Write the key: ")
    print("decryption")
    decrypted_text = ""
    pos = 0
    for i in encrypted_text:
        if (i != '\n'):
            if (pos == len(key)):
                pos = 0
            decrypted_text = decrypted_text + array[array.index(i) - (array.index(key[pos])) % int(32)]
            pos = pos + 1
    print(decrypted_text)
def main():
    name1 = "text.txt"
    encrypt(name1)
    name2 = "encrypted"
    #name2 = "key_ПЕС.txt"
    text = file_content(name2)
    text = del_content(text)
    print("encrypted file`s index", text)
    secs = []
    for i in range(2, 20, 1):
        sections = devide(text, i)
        decrypt(sections)
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("most probable length")
    st_i.sort(reverse=True)
    for item in st_i:
        print(item)
    print(
        "------------------------------------------------------------------------------------------------------------------------------------")

    decryption(array_of_sections)
    decr(name2)
print(array[23])
main()

