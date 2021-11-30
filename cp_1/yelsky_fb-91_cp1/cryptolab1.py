#!/usr/bin/env python
# coding: utf-8

# In[92]:


import regex 
import collections
import unicodedata
import re
import pandas as pd
import numpy as np
import math




kniga = open("/Users/macbook/Downloads/avidreaders.ru__prestuplenie-i-nakazanie-dr-izd.txt").read()
kniga = kniga.replace("\n"," ")
kniga = ' '.join(kniga.split())
kniga = kniga.lower()



string  = ''.join(c for c in kniga if unicodedata.category(c).startswith('L'))


string_space = regex.sub(r'[^\w\s]+|[\d]+', r'',kniga).strip()



print(string)


# In[8]:


get_ipython().system('pip install math')


# In[84]:


latters = []  
latters_space = []
for i in range(0,len(string)):
    latters.append(string[i])
for i in range(0,len(string_space)):
    latters_space.append(string_space[i])
    
latters_count = dict(collections.Counter(latters))
latters_space_count = dict(collections.Counter(latters_space))



# In[85]:


print(latters_count)


# In[86]:


chastota_latters = {key: latters_count[key] / len(latters) for key in latters_count}
chastota_latters_space = {key: latters_space_count[key] / len(latters_space) for key in latters_space_count}
print(chastota_latters)


# In[99]:



table = pd.DataFrame()

table_space = pd.DataFrame()
table['latters'] = chastota_latters.keys()
table_space['latters'] = chastota_latters_space.keys()
table['chastota'] = chastota_latters.values()
table_space['chastota'] = chastota_latters_space.values()



table = table.sort_values(by=['chastota'] , ascending=False)
table_space = table_space.sort_values(by=['chastota'] , ascending=False)
print(table)
table.to_excel("/Users/macbook/Downloads/cryptolab1.1.xlsx")
table_space.to_excel("/Users/macbook/Downloads/crypto_spacelab2.1.xlsx")


# In[46]:


bigram1_space = []
bigram2_space = []
for j in range(0, len(string_space)-1):
    bigram1_space.append(string_space[j]+string_space[j+1])
    
for j in range(0, len(string_space)-2,2):
    bigram2_space.append(string_space[j]+string_space[j+1])


bigram1_space_count = dict(collections.Counter(bigram1_space))
bigram2_space_count = dict(collections.Counter(bigram2_space))

chastota_bigram1_space= {key: bigram1_space_count[key] / len(bigram1_space) for key in bigram1_space}
chastota_bigram2_space= {key: bigram2_space_count[key] / len(bigram2_space) for key in bigram2_space}

print(bigram1_space_count,chastota_bigram1_space)


# In[ ]:


bigram1 = []
bigram2 = []
for j in range(0, len(string)-1):
    bigram1.append(string[j]+string[j+1])
    
for j in range(0, len(string)-2,2):
    bigram2.append(string[j]+string[j+1])


bigram1_count= dict(collections.Counter(bigram1))
bigram2_count= dict(collections.Counter(bigram2))

chastota_bigram1_count= {key: bigram1_count[key] / len(bigram1) for key in bigram1_count}
chastota_bigram2_count= {key: bigram2_count[key] / len(bigram2) for key in bigram2_count}


# In[107]:


def H(chastota,n):
    t = []
    for f in chastota.values():
        t.append(f*math.log(f,2))
    t = sorted(t)
    H = -sum(t)/n
    return H
  
H1 = H(chastota_bigram1_count,2) 
H2= H(chastota_bigram2_count,2) 
H1_space = H(chastota_bigram1_space,2) 
H2_space = H(chastota_bigram2_space,2) 
print(H(chastota_latters,1))
print(H(chastota_latters_space,1))
print(H1)
print(H2)
print(H1_space)
print(H2_space )


# In[106]:


Alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',' з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']
Alphabet_space = [' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',' з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']

def table_of_bigrams( Alphabet, chastota):
    table = pd.DataFrame(index = Alphabet, columns=Alphabet)
    bigrams_ = []
    for i in Alphabet:
        for j in Alphabet:
            bigrams_.append(i+j) 
    n = 0
    for i in range(0,len(Alphabet)):
        table [Alphabet[i]] = bigrams_[n:len(Alphabet)+n]
        n = len(Alphabet)+n
    table = table.T
    import numpy as np
    for key in list(chastota.keys()):
        a,c = np.where(table == key)
        table.iloc[a,c] = chastota[key]
    for m in bigrams_:
        a,c = np.where(table == m)
        table.iloc[a,c] = 0
    return table


#matrix_bigram1_count =  table_of_bigrams(Alphabet,chastota_bigram1_count )
#matrix_bigram2_count =  table_of_bigrams(Alphabet,chastota_bigram2_count )
#matrix_bigram1_space =  table_of_bigrams(Alphabet_space,chastota_bigram1_space )
matrix_bigram2_space =  table_of_bigrams(Alphabet_space,chastota_bigram2_space )



#matrix_bigram1_count.to_excel("/Users/macbook/Downloads/cryptomatrix1.xlsx")
#matrix_bigram2_count.to_excel("/Users/macbook/Downloads/cryptomatrix2.xlsx")
#matrix_bigram1_space.to_excel("/Users/macbook/Downloads/cryptomatrix3.xlsx")
#matrix_bigram2_space.to_excel("/Users/macbook/Downloads/cryptomatrix4.xlsx")
print(matrix_bigram2_space)


# In[78]:


print(Alphabet_space)


# In[ ]:





# In[ ]:




