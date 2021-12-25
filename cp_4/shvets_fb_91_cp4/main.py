from random import randint
import random



def gorner(x, e, n):
    bin_e = bin(e)
    y = 1
    for i in range(len(bin_e) - 2):
        y = (y ** 2) % n
        if int(bin_e[i + 2]) == 1:
            y = (x * y) % n
    return y

# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
    # Initialize result
    res = 1;

    # Update x if it is more than or
    # equal to p
    x = x % p;
    while (y > 0):

        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;

        # y must be even now
        y = y >> 1;  # y = y/2
        x = (x * x) % p;

    return res;


# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4);

    # Compute a^d % n
    x = power(a, d, n);

    if (x == 1 or x == n - 1):
        return True;

    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;

        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

    # Return composite
    return False;


# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def isPrime(n, k):
    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;

    # Iterate given nber of 'k' times
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;

    return True;


# Driver Code
# Number of iterations
k = 4;


def rand_number():
    numb = randint(2 ** 256, 2 ** 260)
    while numb % 2 == 0:
        numb = randint(2 ** 256, 2 ** 260)
    return numb

pair_A = []
pair_B = []
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
def generate_pair():
    pair_A.append(rand_number())
    if isPrime(pair_A[0], 4) == False:
        while isPrime(pair_A[0], 4) == False:
            print("False: ", pair_A[0])
            pair_A[0] = rand_number()
    pair_A.append(rand_number())
    if isPrime(pair_A[1], 4) == False:
        while isPrime(pair_A[1], 4) == False:
            pair_A[1] = rand_number()
    pair_B.append(rand_number())
    if isPrime(pair_B[0], 4) == False:
        while isPrime(pair_B[0], 4) == False:
            pair_B[0] = rand_number()
    pair_B.append(rand_number())
    if isPrime(pair_B[1], 4) == False:
        while isPrime(pair_B[1], 4) == False:
            pair_B[1] = rand_number()
    if(pair_A[0]*pair_A[1] < pair_B[0]*pair_B[1]):
        pair_A.clear()
        pair_B.clear()
        return generate_pair()
    else:
        pair_A.append(pair_A[0] * pair_A[1])
        pair_B.append(pair_B[0] * pair_B[1])
        pair_A.append((pair_A[0] - 1) * (pair_A[1] - 1))
        pair_B.append((pair_B[0] - 1) * (pair_B[1] - 1))
# This code is contributed by mits


def alg_e(x, size):
    size_buf = size
    rs = []
    coef = [0, 1]
    bsize = size
    while x != 0 and size != 0:
        if x > size:
            rest = x % size
            r = (x - rest) / size
            rs.append(-r)
            x = x % size
        else:
            rest = size % x
            r = (size - rest) / x
            rs.append(-r)
            size = size % x
        # rest_for_a_and_b = a+b
        # print(" is ", rest_for_a_and_b)
    for i in range(0, len(rs), 1):
        coef.append(rs[i] * coef[-1] + coef[-2])
    print(rs)
    print(coef)
    if (coef[-2] < 0):
        a = bsize + coef[-2]
    else:
        a = coef[-2]
    print("a - ", a)
    return a
def get_e(pair):
    e = randint(2, pair[3])
    return e
def Encrypt(M, pair, key):


    C = gorner(M, key, pair[2])

    C = gorner(M, key, pair[2])

    return C
def Decrypt(C, pair, pair2):
    return gorner(C, pair, pair2)
def Sign(M, pair):
    C = gorner(M, pair[5], pair[2])
    return C
def kpi_re(a, b):
    def euclid(a, b):
        if not b:
            return 1, 0, a
        y, x, d = euclid(b, a % b)
        return x, y - (a // b) * x, d

    x, _, _ = euclid(a, b)
    return x
def Verify(M, final_result):
    if M == final_result:
       print("Signature is verified")
arr = []
def Send():
    S = Sign(M, pair_A)
    S1 = Encrypt(S, pair_B, pair_B[4])
    k1 = Encrypt(M, pair_B, pair_B[4])
    arr.append(k1)
    arr.append(S1)
    arr.append(S)
    print("A sends confidential key to B(RSA):")
    print("S - ", S)
    print("S1 - ", S1)
    print("k1 - ", k1)
def Receive(pair_A, pair_B, M):
    k_B = Decrypt(arr[0], pair_B[5], pair_B[2])
    S_B = Decrypt(arr[1], pair_B[5], pair_B[2])
    final_result = Decrypt(arr[2], pair_A[4], pair_A[2])
    print("k_B - ", k_B)
    print("S_B - ", S_B)
    print("signature - ", final_result)
    Verify(M, final_result)

generate_pair()
#print(len(str(pair_A[0])))
#print(pair_B)
#print(miller(pair_A[0], 10))
print("first number in A is Prime: ", isPrime(pair_A[0], k))
print("second number in A is Prime: ",isPrime(pair_A[1], k))
print("first number in B is Prime: ",isPrime(pair_B[0], k))
print("second number in A is Prime: ",isPrime(pair_B[1], k))




print("a", len(str(156962848314868059556431134966166206740777217306021974382558216785568212759799268227260499237979741587764149503287590182472188438280084531957681124715481401)))
M = randint(10000000000000000000000000000000000, 99999999999999999999999999999900000000000000000000000000)
text = randint(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999000000000000000000000000000000000000000000000000000000000000000000000000)
print("RSA key - ", hex(M))
print(isPrime(pair_A[0], k))
print(isPrime(pair_A[1], k))

pair_A.append(get_e(pair_A))
while gcd(pair_A[3], pair_A[4]) != 1:
    pair_A[4] = get_e(pair_A)
pair_B.append(get_e(pair_B))
while gcd(pair_B[3], pair_B[4]) != 1:
    pair_B[4] = get_e(pair_B)
#--------------------------------------------------------------------------------------------------
#First send ecrypted text than the 2 decrypts

pair_A.append(kpi_re(pair_A[4], pair_A[3]) % pair_A[3])
pair_B.append(kpi_re(pair_B[4], pair_B[3]) % pair_B[3])

#--------------------------------------------------------------------------------------------------

print("keys for A: ")
print("p - ", pair_A[0])
print("q - ", pair_A[1])
print("n - ", pair_A[2])
print("u - ", pair_A[3])
print("d - ", pair_A[4])
print("keys for B: ")
print("p - ", pair_B[0])
print("q - ", pair_B[1])
print("n - ", pair_B[2])
print("u - ", pair_B[3])
print("d - ", pair_B[4])
#print(pair_B)
#pair_A.append(kpi_re(pair_B[4], pair_B[3]) % pair_B[3])
print("Some text: ", text)
textA = Encrypt(M, pair_A, pair_A[4])
print("Encrypted by A key: ", textA)
textB = Encrypt(M, pair_B, pair_B[4])
print("Encrypted by B key: ", textB)


    #print("#", Decrypt(S, pair_A[4], pair_A[2]))
Send()
#--------------------------------------------------------------------------------------------------

Receive(pair_A, pair_B, M)
#verify(pair_A, pair_B)


M = 21
pair_test = [41, 17, 697, 640]
#print(isPrime(pair_test[0], k))
#print(isPrime(pair_test[1], k))
#Encrypt(M, pair_test)
#print(alg_e(17, 37))

print("hex A e", hex(pair_A[4]))
print("M hex", hex(pair_A[2]))
print("k1 hex ", hex(arr[0]))
print("S1 hex ", hex(arr[1]))

