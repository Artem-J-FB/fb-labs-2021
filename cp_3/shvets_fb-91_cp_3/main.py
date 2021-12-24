import math
array = [u"А", u"Б", u"В", u"Г", u"Д", u"Е", u"Ж", u"З", u"И", u"Й", u"К", u"Л", u"М", u"Н", u"О", u"П", u"Р", u"С", u"Т", u"У", u"Ф", "Х", "Ц", u"Ч", u"Ш", u"Щ", u"Ы", u"Ь", u"Э", u"Ю", u"Я"]
freq_bi = ["СТ", "НО", "ТО", "НА", "ЕН"]
def file_content(name):
    f = open(name, "r", encoding="UTF-8")
    text_of_the_file = ""
    for lines in f.readlines():
        text_of_the_file = text_of_the_file + lines
    f.close()
    return text_of_the_file

def del_content(text):
    text2 = ""
    new_text = text.upper().replace("Ё","Е").replace("Ъ","Ь").replace(" ", "").replace("\n","").replace(".","").replace("-","").replace(",","").replace(" ","").replace(":","").replace("!","")
    return new_text
bigram = []
all_bigrams = []
bigrams_frequency = []
main_list = []
buf = []
def bigrams(text):
    for i in range(0, len(text), 2):
        bi = ""
        bi = text[i] + text[i + 1]
        all_bigrams.append(bi)
        if(bigram.count(bi) == 0):
            bigram.append(bi)
    for i in range(0, len(bigram), 1):
        fr = count_frequency(bigram[i])
        bigrams_frequency.append(fr)
    print(len(bigrams_frequency))
    print(len(bigram))
    print(all_bigrams)
    for i in range(0, len(bigram)):
        main_list.append((bigrams_frequency[i], bigram[i]))
def count_frequency(bi):
    return all_bigrams.count(bi)/len(all_bigrams)
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
def alg_e(sub_y, sub_x, size):
    size_buf = size
    rs = []
    coef = [0, 1]
    bsize = size
    while sub_x != 0 and size != 0:
        if sub_x > size:
            rest = sub_x % size
            r = (sub_x - rest) / size
            rs.append(-r)
            sub_x = sub_x % size
        else:
            rest = size % sub_x
            r = (size - rest) / sub_x
            rs.append(-r)
            size = size % sub_x
        # rest_for_a_and_b = a+b
        # print(" is ", rest_for_a_and_b)
    for i in range(0, len(rs), 1):
        coef.append(rs[i] * coef[-1] + coef[-2])
    #print(rs)
    #print(coef)
    if (coef[-2] < 0):
        a = bsize + coef[-2]
    else:
        a = coef[-2]
    #print("a - ", a)
    result_a = a * sub_y
    if(result_a > size):
        result_a = result_a%size_buf
    return result_a
all_solutions = []
all_b = []
def calculate_b(size):
    for i in all_solutions:
        b = (i[0] - i[4]*i[2])%size
        #print("b - ", b)
        all_b.append(b)
        #all_solutions[i].append(b)
        #all_solutions[i].append(b2)
reverse_a = []
index = []
def alg(y1, y2, x1, x2, size):
    sub_y = y1 - y2
    sub_x = x1 - x2
    if(sub_x < 0):
        while sub_x < 0:
            sub_x = sub_x + size
    if (sub_y < 0):
        while sub_y < 0:
            sub_y = sub_y + size
    gcd_res = gcd(sub_x, size)
    if(gcd_res == 1):
        result_a = alg_e(sub_y, sub_x, size)
        if(result_a == 728):
            print(result_a)
        all_solutions.append((y1, y2, x1, x2, result_a))
    if (gcd_res > 1 and sub_y%gcd_res == 0):
        result_temp = alg_e(sub_y/gcd_res, sub_x/gcd_res, size/gcd_res)
        result_temp = result_temp%(size/gcd_res)
        #print(result_temp)
        for i in range(0, gcd_res, 1):
            result_a = result_temp + i*size/gcd_res
            all_solutions.append((y1, y2, x1, x2, result_a))
            if (result_a == 728):
                print(result_a)

most_frequent_X = ["СТ", "НО", "ТО", "НА", "ЕН"]
X_index = []
most_frequent_Y = []
Y_index = []
most_frequent = []
def sort_list(slist):
    for i in range(0, 5, 1):
        most_frequent_Y.append(slist[i][1])
index_of_bigrams = []
def count_index(mfrequent, a):
    for i in range(len(mfrequent)):
        a.append(array.index(mfrequent[i][0])*len(array)+array.index(mfrequent[i][1]))
right_solutions = []
def check_text():
    count_index(all_bigrams, index_of_bigrams)
matched = []
def filter(letters, words):
    msum = 0
    for i in words:
        msum = msum + letters.count(i.upper())
        if(letters.count(i.upper()) > 0):
            print("I gave found ", i)
            print(letters)
    return msum
all_decrypted_texts = []

def decrypt(decrypted_text):
    letters = ""
    for ind in range(len(decrypted_text)):
        ind = int(ind)
        a = (decrypted_text[ind] - decrypted_text[ind] % len(array)) / len(array)
        a = int(a)
        first_letter = array[a]
        b = decrypted_text[ind] % len(array)
        b = int(b)
        second_letter = array[b]
        letters = letters + first_letter + second_letter
    return letters
entropy_of_letters = []
def entropy(text, letters_frequency): #search the entropy

    result = 0
    for i in range(0, len(array), 1):
        fr = text.count(array[i])/len(text)
        result = result + (1/1)*fr*math.log(1/fr,2)
    entropy_of_letters.append(result)
    return result
def decryption(text):
    check_text()
    file1 = open("popular_words", "r",  encoding="UTF-8")
    words = file1.readlines()

    # закрываем файл
    file1.close
    for i in range(len(right_solutions)):
        #print("Trying a - ", right_solutions[i][-1], " and b - ", right_solutions[i][-2])
        decrypted_text = []
        for j in range(len(index_of_bigrams)):
            a = right_solutions[i][-1]*(index_of_bigrams[j] - right_solutions[i][-2])
            decrypted_text.append((a)%(len(array)*len(array)))
        letters = decrypt(decrypted_text)
        if entropy(letters, entropy_of_letters) < 4.5:
            print(right_solutions[i])
            print(letters)
    bb = sorted(entropy_of_letters, reverse=False)
    #print(entropy_of_letters.index(bb[0]))

    #for i in range(len(all_decrypted_texts)):



def main():
    text = del_content(file_content("text"))
    print(len(text))
    bigrams(text)
    slist = sorted(main_list, reverse=True)
    sort_list(slist)
    print(most_frequent_Y)
    print(most_frequent_X)
    count_index(most_frequent_Y, Y_index)
    count_index(most_frequent_X, X_index)
    print(Y_index)
    print(X_index)
    for i in range(len(Y_index) - 1):
        for j in range(i + 1, len(Y_index), 1):
            for m in range(len(X_index) - 1):
                for n in range(m + 1, len(X_index), 1):
                    #print(Y_index[i], Y_index[j], X_index[m], X_index[n], len(array)*len(array))
                    alg(Y_index[i], Y_index[j], X_index[m], X_index[n], len(array)*len(array))
    calculate_b(len(array)*len(array))
    for i in range(len(all_solutions)):
        if gcd(all_solutions[i][-1], len(array)*len(array)) == 1:
            reverse_a.append(alg_e(1, all_solutions[i][-1], len(array)*len(array)))
            index.append(i)
    for i in range(len(index)):
        right_solutions.append((all_solutions[index[i]], all_b[index[i]], reverse_a[i]))
    decryption(text)
main()
for i in right_solutions:
    if(i[-1] == 509):
        print("________", right_solutions.index(i))


print(right_solutions)
print(index_of_bigrams)
