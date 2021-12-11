import random
import math


def miller_rabin(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0:
        return False
    a = 0
    b = num - 1
    while b % 2 == 0:
        b = b // 2
        a = a + 1
    c = b
    for i in range(0, 3):
        m = random.randint(2, num - 1)
        l = pow(m, c, num)
        if l == 1 or l == num - 1:
            continue
        for r in range(0, a - 1):
            l = pow(l, 2, num)
            if l == 1:
                return True
            if l == num - 1:
                break
        else:
            return False
    return True


def generate_key_pair(size):
    i = 0
    prime_list = []
    while i < 4:
        number = random.getrandbits(size)
        print(number)
        x = miller_rabin(number)
        if x:
            prime_list.append(number)
            i += 1
        print(x)
    p = prime_list[0]
    q = prime_list[1]
    print("Prime letters: " + str(list))
    n = p * q
    phi_n = (p - 1) * (q - 1)
    x = False
    e = 0
    while not x:
        e = random.randrange(2, phi_n - 1)
        if math.gcd(e, phi_n) == 1:
            x = True
    d = pow(e, -1, phi_n)
    return (p, q), (e, d, n)



def encrypt(m, keys):
    c = pow(m, keys[1][0], keys[1][2])
    return c


def decrypt(C, keys):
    m = pow(C, keys[1][1], keys[1][2])
    return m


def sign(m, keys):
    s = pow(m, keys[1][1], keys[1][2])
    return s


def verify(m, s, keys):
    if m == pow(s, keys[1][0], keys[1][2]):
        return True
    else:
        return False


def send_key(k, keys_b, keys_a):
    k1 = pow(k, keys_b[1][0], keys_b[1][2])
    s = pow(k, keys_a[1][1], keys_a[1][2])
    s1 = pow(s, keys_b[1][0], keys_b[1][2])
    print("Message was sent")
    return k1, s1, s


def receive_key(k1, s1, keys_b, keys_a):
    k = pow(k1, keys_b[1][1], keys_b[1][2])
    s = pow(s1, keys_b[1][1], keys_b[1][2])
    if k == pow(s, keys_a[1][0], keys_a[1][2]):
        print("Message was verified!")
        return k, s
    else:
        print("Message wasn't verified!")
        return False


keys_A = generate_key_pair(256)
keys_B = generate_key_pair(256)
while keys_A[0][0] * keys_A[0][1] >= keys_B[0][0] * keys_B[0][1]:
    keys_B = generate_key_pair(256)
print("p: " + str(keys_A[0][0]))
print("q: " + str(keys_A[0][1]))
print("p1: " + str(keys_B[0][0]))
print("q1: " + str(keys_B[0][1]))
print("e: " + str(keys_A[1][0]))
print("d: " + str(keys_A[1][1]))
print("n: " + str(keys_A[1][2]))
print("e1: " + str(keys_B[1][0]))
print("d1: " + str(keys_B[1][1]))
print("n1: " + str(keys_B[1][2]))
k = random.randrange(1, keys_A[1][0] - 1)
print("k: " + str(k))
plain_text = random.randrange(1, keys_A[1][0] - 1)
print("PT: " + str(plain_text))

# test for A
c = encrypt(plain_text, keys_A)
print("c_A: " + str(c))
m = decrypt(c, keys_A)
print("m: " + str(m))
s = sign(m, keys_A)
print("s_A: " + str(s))
print(verify(m, s, keys_A))

# test for B
c = encrypt(plain_text, keys_B)
print("c-B: " + str(c))
m = decrypt(c, keys_B)
print("m: " + str(m))
s = sign(m, keys_B)
print("s_B: " + str(s))
print(verify(m, s, keys_B))

k1, s1, s = send_key(k, keys_B, keys_A)
print("From A to B")
print("k1: " + str(k1))
print("s1: " + str(s1))
receive_key(k1, s1, keys_B, keys_A)

temp_keys_B = ((keys_B[0][0], keys_B[0][1]), (int("10001", 16), keys_B[1][1], int(
     "DD974493B02EDF6BF2BBADCC58C89370CC20FE30C063A316C9F00D70D417F3929430F04116129827A3B4D10B68A44E789C96A15BCF8292AE830094CF3B160757",
     16)))
k1, s1, s = send_key(k, temp_keys_B, keys_A)
print("k1 = ", hex(k1))
print("s1 = ", hex(s1))
print("s = ", hex(s))
print(hex(keys_A[1][0]))
print(hex(keys_A[1][2]))
