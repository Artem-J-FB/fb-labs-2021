import random
import math


def fast_pow(x, pow_num, mod):
    e = bin(pow_num)[2:]
    y = 1
    for i in e:
        y = (pow(y, 2)) % mod
        if int(i) == 1:
            y = (x * y) % mod
    return y


def miller_rabin(n, k=40):
    for i in range(k):
        a = random.randrange(2, n - 1)
        exp = n - 1
        while not exp & 1:
            exp >>= 1

        if fast_pow(a, exp, n) == 1:
            return True

        while exp < n - 1:
            if fast_pow(a, exp, n) == n - 1:
                return True

            exp <<= 1

        return False

    return True


def gen_prime(bits):
    while True:
        a = (random.randrange(2 ** (bits - 1), 2 ** bits))
        if miller_rabin(a):
            return a



def euclid(a, b):
    if not b:
        return 1, 0, a
    y, x, d = euclid(b, a % b)
    return x, y - (a // b) * x, d


def re(a, b):
    x, _, _ = euclid(a, b)
    return x


def GenerateKeyPair(p, q):
    n = p * q
    fn = (p - 1) * (q - 1)
    e = random.randrange(2, fn - 1)
    while math.gcd(e, fn) != 1:
        e = random.randrange(2, fn - 1)
    d = re(e, fn)%fn
    return d, n, e


def encrypt(M, e, n):
    C = fast_pow(M, e, n)
    return C


def decrypt(C, d, n):
    M = fast_pow(C, d, n)
    return M


def sign(M, d, n):
    S = fast_pow(M, d, n)
    return S


def verify(M, S, e, n):
    return M == fast_pow(S, e, n)


def SendKey(k,e1,n1, S):
    k1 = fast_pow(k,e1,n1)
    S1 = fast_pow(S,e1,n1)
    return k1,S1

def ReceiveKey(k1,S1,d1,n1):
    k = fast_pow(k1,d1,n1)
    S = fast_pow(S1,d1,n1)
    return k, S

def auth(S, e, n):
    k = fast_pow(S, e, n)
    return k


# p, q, p1, q1 = generate_primes()
p = 74922627183685304053722884322805637745690272692523044793486349668123438040829
q = 75324767041681899148494173923250897223405873538487952032903781718006914781417
p1 = 111901671628977001564147404942096238930976310155236920828452624871953481725621
q1 = 95361536723636825973566889979596239333188200025823244746304352097879684478703

d, n, e = GenerateKeyPair(p, q)

d1, n1, e1 = GenerateKeyPair(p1, q1)
print('n: ',n,'\ne:',e,'\nd:',d)
# M = random.randint(0,n)
M = 1848071151586865208136788829907359312232716431938205295121696102514916928375815365197506529614363687569594640829234893520859494305204668393401028932482696
C = encrypt(M, e, n)
M_test = decrypt(C, d, n)

print("M: ", M)
print("C: ", C)

f = (p - 1) * (q - 1)
print("f:", f)

print("Text verification: ", M == M_test)


k = random.randint(0,n)
S = sign(k, d, n)

K1, S1 = SendKey(k, e1, n1, S)
K, S_rec = ReceiveKey(K1, S1, d1, n1)
k_rec = auth(S, e, n)
print("Key verification: ", k == k_rec)


