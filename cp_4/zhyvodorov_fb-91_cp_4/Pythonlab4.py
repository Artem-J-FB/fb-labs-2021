import random



def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def mod_pow(a,b,m): 
    b_bin= bin(b)[2:]
    Y = 1
    for i in b_bin:
        Y = Y ** 2 % m
        Y = Y * (a ** int(i)) % m 
    return Y

def conv(n,ri,ro):
    digs="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc=0
    for a in n:
        k=digs.find(a)
        acc=acc*ri+k
    res=""
    while(acc>0):
        k=acc%ro
        res=digs[k]+res
        acc=acc//ro
    return res 

def MiLr(num, k):
    r = 0
    d = num - 1
    while d % 2 == 0:
        r= r+1
        d = d // 2
    #print(num," = ", d, " * ", 2," ** ", r)
    for _ in range (k):
        a = random.randrange(2, num - 1)
        if gcd(num,a) > 1:
            return False
        else:
            x = mod_pow(a,d,num)
            if x == 1 or x == num-1:
                continue
                for _ in range(r-1):
                    x = mod_pow(x,2,num)
                    if x == num - 1:
                        break
            return False
    return True


def get_num():
    number = random.randrange(2 ** 256, 2 ** 258)
    while number % 2 == 0:
         number = random.randrange(2 ** 256, 2 ** 258)
    return number



def get_prime():
    number = get_num()
    while MiLr(number, 40) != True:
        number = get_num()
    return number


def Create_keys():
    p1 = get_prime()
    p2 = get_prime()
    n = p1 *  p2
    fiN= (p1-1) * (p2 -1)
    e = 2 ** 16 + 1
    d = modinv(e,fiN)
    return e,d,n

def Encrypt(M,e,n):
    return mod_pow(M,e,n)

def Decrypt(C,d,n):
    return mod_pow(C,d,n)

def Sign(M,d,n):
    return mod_pow(M,d,n)

def Prove(M,S,e,n):
    if M== mod_pow(S,e,n):
        return True
    return False

def Send_Key(e1,n,n1,d,k):
    S = mod_pow(k,d,n)
    S1 = mod_pow(S,e1,n1)
    k1 = mod_pow(k,e1,n1)
    return k1,S1

def Receive_Key(k1,S1,d1,n1,e,n):
    k = mod_pow(k1,d1,n1)
    S = mod_pow(S1,d1,n1)
    if k == mod_pow(S,e,n):
        return k
    return 0

e1,d1,n1 = Create_keys()
e2,d2,n2 = Create_keys()


M = 123456789
C = Encrypt(M,e1,n1)
Modulus = conv(str(n1), 10,16)
print("Modulus ",Modulus)
Ciphertext = conv(str( C ), 10,16)
print("Ciphertext ",Ciphertext)
Message = conv(str(M), 10,16)
print("Message ",Message)

M = Decrypt(C,d1,n1)
print(M)

S= Sign(M,d1,n1)
Sign = conv(str(S), 10,16)
Modulus = conv(str(n1), 10,16)
Message = conv(str(M), 10,16)
print("Message ",Message)
print("Sign ",Sign)
print("Modulus ",Modulus)
E1 = conv(str(e1), 10,16)
print("Public exponent ",E1)


if Prove(M,S,e1,n1):
    print("Proved")

if n1 < n2:
    k1,S1 = Send_Key(e1,n1,n2,d1,54321)
    k = Receive_Key(k1,S1,d2,n2,e1,n1)
else:
    k1,S1 = Send_Key(e2,n2,n1,d2,54321)
    k = Receive_Key(k1,S1,d1,n1,e2,n2)
print(k)


