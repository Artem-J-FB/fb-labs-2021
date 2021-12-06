#!/usr/bin/env python
# coding: utf-8

# In[412]:


import random
def Miller_Rabin_test(number, k):
    number = int(number)
    if number%2 == 0 or number%3==0 or number%4==0 or number%5==0 or number%6 ==0 or number%7==0 or number%8==0 or number%9 == 0 or number%10==0:
        return False
    if number<=3 and number>1:
        return True
    if number == 1:
        return False
    s = 0
    d = number-1
    while d%2==0:
        d = d//2
        s = s+1
    t = int(d)
    for i in range(0,k):
        a = random.randint(2,number-1)
        x = pow(a,t,number)
        if x == 1 or x == number - 1:
            continue
        for r in range(0, s-1):
            x = pow(x,2,number)
            if x == 1: 
                return True
            if x == number-1:
                break
        else:
            return False
    return True

    


# In[425]:


Miller_Rabin_test(q1,4)


# In[420]:


def search_number():
    number = random.getrandbits(256)
    #print(number)
    #print(Miller_Rabin_test(number, 256))
    while Miller_Rabin_test(number, 4) == False:
        print(number)
        print(Miller_Rabin_test(number, 4))
        number = random.getrandbits(256)
    return number


# In[421]:


numbers = []
while(len(numbers)<4):
    a = search_number()
    for i in range(0, len(numbers)):
        if (a!=numbers[i]):
            numbers.append(a)



# In[99]:


for i in range(1,4):
    if(numbers[0]*numbers[i]<numbers[(i+1)%4]*numbers[(i+2)%4]):
        p = numbers[0]
        q = numbers[i]
        p1 = numbers[(i+1)%4]
        q1 = numbers[(i+2)%4]
        break   
    


# In[240]:


p = 452312848583266388373324160190187140051835877600158453279131187530910662655971
q = 452312848583266388373324160190187140051835877600158453279131187530910662656031
p1 = 452312848583266388373324160190187140051835877600158453279131187530910662656093
q1 = 452312848583266388373324160190187140051835877600158453279131187530910662656409


# In[263]:


print("\n",p,"\n",q,"\n",p1,"\n",q1)


# In[249]:


q1.bit_length() 


# In[268]:


def euclid(a, b):
    if b == 0:  
        return a, 1, 0
    else:
        d, x, y = euclid(b, a % b)
        return d, y, x - y * (a // b)
    
def obr(a,mod):
    return euclid(a,mod)[1]%mod


# In[314]:


e = random.randint(2,fn-1)
euclid(e,fn-1)


# In[435]:


def GenerateKeyPair(p,q):
    n = p*q
    fn = (p-1)*(q-1)
 
    e = random.randint(2,fn-1)
    while euclid(e,fn)[0]!=1:
         e = random.randint(2,fn-1)
   
    d = obr(e,fn)
    return n,e,d,fn


# In[ ]:


def encrypt(n,e,M):
    C = pow(M,e,n)
    return C


# In[436]:


n,e,d,fn = GenerateKeyPair(p,q)
n1,e1,d1,fn1 = GenerateKeyPair(p1,q1)

n<n1


# In[446]:


print('n: ',n,'\ne:',e,'\nd:',d)
print('\n\nn: ',n1,'\ne:',e1,'\nd:',d1)


# In[440]:


import math

print (math.gcd (e1, fn1))


# In[447]:


M = random.randint(0,n)
C = encrypt(n,e,M)


# In[448]:


M


# In[449]:


def decrypt(C,d,n):
    M = pow(C,d,n)
    return M


# In[454]:


M


# In[453]:


C


# In[450]:


M = decrypt(C,d,n)
M


# In[367]:


def Sign(M,d,n):
    S = pow(M,d,n)
    return S


# In[451]:


S = Sign(M,d,n)
S


# In[326]:


def verify(M,S,e,n):
    return M == pow(S,e,n)


# In[452]:


verify(M,S,e,n)


# In[462]:


k = random.randint(0,n)
k


# In[463]:


n1>n


# In[460]:


d1


# In[467]:


def SendKey(k,e1,n1):
    k1 = pow(k,e1,n1)
    S1 = pow(S,e1,n1)
    return k1,S1
k1,S1 = SendKey(k,e1,n1)
S = pow(k,d,n)
print('k1: ',k1,"\n\nS1: ",S1,"\n\nS: ",S)


# In[386]:


def ReceiveKey(k1,S1,d1,n1):
    k = pow(k1,d1,n1)
    S = pow(S1,d1,n1)
    return k,S


# In[370]:


def verifysigh(k,S,e):
    return k ==pow(S,e,n)


# In[469]:


k,S = ReceiveKey(k1,S1,d1,n1)
print('k: ',k,'\nS: ',S)


# In[470]:


verifysigh(k,S,e)


# In[389]:


k


# In[390]:


pow(S,e,n)


# In[ ]:




