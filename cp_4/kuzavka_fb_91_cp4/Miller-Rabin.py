#!/usr/bin/env python3

import random

def MillerRabin(n):
    d = 0
    ec = n-1
    while ec % 2 == 0:
        ec >>= 1
        d += 1
    assert(pow(2, d) * ec == n-1)
    
    # 20 rounds
    for i in range(40):
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


print('Newly generated prime number is:', getPrime(256))
