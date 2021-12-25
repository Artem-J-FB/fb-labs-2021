#!/usr/bin/env python3

import time
import random
import math

def MillerRabin(n):
    d = 0
    ec = n-1
    while ec % 2 == 0:
        ec >>= 1
        d += 1
    assert(pow(2, d) * ec == n-1)
    
    # 20 rounds
    for i in range(200):
        t = random.randrange(2, n)
        if pow(t, ec, n) == 1:
            passed = False
        for i in range(d):
            if pow(t, pow(2,i) * ec, n) == n-1:
                passed = False
        passed = True
        
        if not passed:
            return False
    return True

def divisionCheck(c):
    if c % 2 == 0:
        return False
    for i in range(3, 999, 2):
        if c % i == 0 and pow(i, 2) <= c:
            return False
    return True

def getPrime(size):
    candidate = 0
    while True:
        while True:
            c = random.randrange(pow(2,(size-1))+1, pow(2,size)-1)
            if divisionCheck(c):
                candidate = c
                break

        if not MillerRabin(candidate):
            continue
        else:
            return candidate

def GenerateKeyPair(keySize):
    # 1 p and q
    p = getPrime(keySize)
    q = getPrime(keySize)

    N = p*q
    phi_N = (p-1)*(q-1)
    e = -1
    while True:
        #e = random.randrange(2, pow(2, keySize))
        e = random.randrange(2, 99)
        if math.gcd(e, phi_N) == 1:
            break

    d = pow(e, -1, phi_N)

    return((e, N), (d, N)) # encrypt key and decrypt key

def Encrypt(PT, key):
    cipherText = ''
    for char in PT:
        cipherText += str(pow(ord(char), key[0], key[1]))
        cipherText += ','
    return cipherText

def Decrypt(CT, key):
    cipherText = CT.split(',')
    plainText = ''
    for num in cipherText:
        if num == '':
            break
        plainText += chr(pow(int(num), key[0], key[1]))
    return plainText

def Verify(sign, signature, key):
    if Decrypt(sign, key) == signature:
        return True
    else:
        return False

def Sign(signature, key):
    return Encrypt(signature, key) # sign

def SendKey(k, e, m, d, N):
    return [pow(k, e, m), pow(pow(k, d, N), e, m)]

def ReceiveKey(k, s, d, N):
    return [pow(k, d, N), pow(s, d, N)]

for chell in ['A','B']: # Write the generated keys into files.
    keys = GenerateKeyPair(256)
    
    f = open(chell + '.enc', 'w')
    f.write(str(keys[0][0]))
    f.write(',')
    f.write(str(keys[0][1]))
    f.close()
    
    f = open(chell + '.dec', 'w')
    f.write(str(keys[1][0]))
    f.write(',')
    f.write(str(keys[1][1]))
    f.close

# Read the key, transfor into the suitable format (touple).
f = open('A.enc', 'r')
A_key = f.read().split(',')
A_key = (int(A_key[0]), int(A_key[1]))
f.close()

# Encrypt the plain text.
PT =\
"          (                 ,&&&.\n\
            )                .,.&&\n\
           (  (              \=__/\n\
               )             ,'-'.\n\
         (    (  ,,      _.__|/ /|\n\
          ) /\ -((------((_|___/ |\n\
        (  // | (`'      ((  `'--|\n\
      _ -.;_/ \\--._      \\ \-._/.\n\
     (_;-// | \ \-'.\    <_,\_\`--'|\n\
     ( `.__ _  ___,')      <_,-'__,'\n\
      `'(_ )_)(_)_)'"
f = open('A_ciphertext.txt', 'w')
f.write(Encrypt(PT, A_key))
f.close

# Read the key, transfor into the suitable format (touple).
f = open('A.dec', 'r')
A_key = f.read().split(',')
A_key = (int(A_key[0]), int(A_key[1]))
f.close()

# Decrypt the data in the 'A_ciphertext.txt' file.
f = open('A_ciphertext.txt', 'r')
print('Decrypted text is:\n', Decrypt(f.read(), A_key))
f.close()

signature = "Artem Kuzavka -- 37166241462974278584796992491942989434912300697696693151628405717819484520158879812718529426796359012673563079141576651901298573"
# Sign
f = open('A.enc', 'r')
A_key = f.read().split(',')
A_key = (int(A_key[0]), int(A_key[1]))
f.close()
sign = Sign(signature, A_key)
print(sign)
# Verify
f = open('A.dec', 'r')
A_key = f.read().split(',')
A_key = (int(A_key[0]), int(A_key[1]))
f.close()
print('\n\nThe signature was successfully verified:', Verify(sign, signature, A_key))


