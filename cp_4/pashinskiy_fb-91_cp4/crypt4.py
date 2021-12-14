import random
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def euclidobrat(c, mod):
    if c < 0:
        c = mod + c
    u1 = mod
    u2 = 0
    v1 = c
    v2 = 1
    while v1 != 0:
        q = u1 // v1
        t1 = u1 - q * v1
        t2 = u2 - q * v2
        u1 = v1
        u2 = v2
        v1 = t1
        v2 = t2
    if u1==1:
        return (u2 + mod) % mod 
    else: 
        return -1
  


def tmr(p,k):
    if p % 2 == 0 or p % 3 == 0 or p % 5 == 0 or p % 7 == 0 or p % 11 == 0:
        return False
    n = p - 1
    s = 0
    while n % 2 == 0:
        s=s+1
        n = n // 2
    d =int(str(n),10);
    for i in range(0,k):
        x = random.randint(1,p-1)
        if gcd(x, p) > 1:
            return False
        else:
            x=pow(x, d ,p)
            if abs(x) == 1:
                return True;
            else:
            
                for i in range(1,s):
                    x =pow(x, 2 ,p)
                    if x == 1:
                        return False
                    elif x == -1:
                        return True
        return False


def generatekey(n):
    x=random.getrandbits(n)
    while tmr(x,4)==False:
        x=random.getrandbits(n)
    return x

def check(n):
    p=1
    q=1
    p1=0
    q1=0
    while p*q>p1*q1:
        q=generatekey(n)
        p=generatekey(n)
        q1=generatekey(n)
        p1=generatekey(n)
    print('P:',p)
    print('q:',q)
    return (q,p,q1,p1)


def GenerateKeyPair(p,q):
    n=p*q
    en=(p-1)*(q-1)
    e=random.randint(2,en-1)
    while gcd(e,en)!=1:
        e=random.randint(2,en-1)
    d=euclidobrat(e,en)
    return n,e,d

def encrypt(m,e,n):
    c=pow(m,e,n)
    return c

def decrypt(c,d,n):
    m=pow(c,d,n)
    return m

def sign(m,d,n):
    s=pow(m,d,n)
    return s

def verify(m,s,e,n):
    if m==pow(s,e,n):
        return True
    else:
        return False

def send(k,d,n,e1,n1):
    k1=pow(k,e1,n1)
    s=pow(k,d,n)
    s1=pow(s,e1,n1)
    return s,k1,s1

def recieve(k1,s1,d1,n1):
    k=pow(k1,d1,n1)
    s=pow(s1,d1,n1)
    return k,s


n1=0
n=1
while n1<n:
    q,p,q1,p1=check(256)
    n,e,d=GenerateKeyPair(p,q)
    n1,e1,d1=GenerateKeyPair(p1,q1)
print('A keys:')
print('n:',n)
print('e:',e)
print('d:',d)
print('B keys:')
print('n:',n1)
print('e:',e1)
print('d:',d1)
k=random.randint(1,n-1)
print('Message:',k)
c=encrypt(k,e,n)
m=decrypt(c,d,n)
print('k(A key check):',k)
print('m:',m)
c=encrypt(k,e1,n1)
m=decrypt(c,d1,n1)
print('k(B key check):',k)
print('Message:',m)
sB=sign(k,d1,n1)
if verify(k,sB,e1,n1):
    print('B sms veirfied')
sA=sign(k,d,n);
if verify(k,sA,e,n):
    print('A sms veirfied')
s,k1,s1=send(k,d,n,e1,n1)
print('A sended k:',k)
print('s:',s)
print('s1:',s1)
kB,s=recieve(k1,s1,d1,n1)
print('B recieved k:',kB)
print('s:',s)
if verify(kB,s,e,n):
    print('Verified')

