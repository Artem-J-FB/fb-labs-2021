import math
import random
import time

def test_miller_rabin(p,k):
	if p <= 1 or p == 4:
		return False
	if p <= 3 or p == 5:
		return True
	if p%2 == 0 or p%3==0 or p%4==0 or p%5==0 or p%6 ==0 or p%7==0 or p%8==0 or p%9 == 0 or p%10==0:
		return False
	# for i in range(3, 999, 2):
	# 	if p % i == 0 and pow(i, 2) <= p:
	# 		return False
	else:
		d,s = rozklad(p)
		for i in range(0,k):
			x = random.randrange(2, p-1)
			# if gcd(x,p)>1:
			# 	return False
			# elif gcd(x,p)==1:
			a = pow(x, d,p)
			if a == 1 or a == p-1:
				continue
			else:
				i=0
				while i<s-1:
					a = pow(a,2)%p
					if a == 1:
						return False
					elif a == p-1:
						break
					else:
						i+=1
				if i==s-1:
					return False
		return True

def rozklad(p):
	counter = p-1
	s=0
	while counter%2==0:
		s+=1
		counter=counter//2
	d = int(counter)
	return(d,s)

def generate_key(size):
	while True:
		x = random.randrange(pow(2,size-1)+1, pow(2,size)-1)
		print(x)
		if test_miller_rabin(x, 4):
			print("__________________________________")
			return x


# condition = True
# while condition:
# 	for i in range(0,4):
# 		q = generate_key(256)
# 		p =	generate_key(256)
# 		q1 = generate_key(256)
# 		p1 = generate_key(256)
# 		if p*q<= p1*q1:
# 			condition = False
# 			print("\n",q,"\n",p,"\n",q1,"\n",p1,"\n")

q = 81994475584405935948868955911630277182389530435402539001816916720392262770879
p = 60695060125406353645205586978113049519423657642692092700480783611828281008489
q1 = 86321480949212574863441223330807749318502228060528766766450179206338212009411
p1 = 81485329224126869631210665457337554019104661539455710371343449787989340245059

def gcd(a, b):
    if b == 0:  
        return a, 1, 0
    else:
        d, x, y = gcd(b, a % b)
        return d, y, x - y * (a // b)

def generate_key_pair(size,p,q):
 # 	q = generate_key(size)
	# p =	generate_key(size)

	n = p*q
	f = (p-1)*(q-1)
	condition = True
	while condition:
		e = random.randrange(2, f-1)
		if gcd(e,f)[0]==1:
			condition = False
	d = int(gcd(e,f)[1])%f
	secret_key = d
	public_key = [n,e]
	return secret_key,public_key

def encrypt(m, e, n):
	c = pow(m,e,n)
	return c

def decrypt(c, d, n):
	m = pow(c,d,n)
	return m

def sign(m, d, n):
	s = pow(m, d, n)
	return s

def verify(m,s,e,n):
	if m == pow(s,e,n):
		return True

def send_key(k, e1, n1, d, n):
	k1 = pow(k,e1,n1)
	s = pow(k,d,n)
	s1 = pow(s,e1,n1)
	return k1,s1,s

def receive_key(k1, s1, d1, n1, s, e, n):
	k = pow(k1,d1,n1)
	s = pow(s1,d1,n1)
	if k== pow(s,e,n):
		print("Message was verified!")
		return k,s
	else:
		print("Message wasn't verified!")
		return False


secret_key_A, public_key_A = generate_key_pair(256, p, q)
secret_key_B, public_key_B = generate_key_pair(256, p1, q1)

print("\n","d =", secret_key_A,"\n","n =", public_key_A[0],"\n","e =", public_key_A[1],"\n","d1 =", secret_key_B,"\n", "n1 =", public_key_B[0],"\n","e1 =", public_key_B[1])
print("\n","d =", hex(secret_key_A),"\n","n =", hex(public_key_A[0]),"\n","e =", hex(public_key_A[1]),"\n","d1 =", hex(secret_key_B),"\n", "n1 =", hex(public_key_B[0]),"\n","e1 =", hex(public_key_B[1]))

k = random.randrange(1, public_key_A[0]-1)
print("\nk =",k)
print("\nk =",hex(k))
m = random.randrange(1, public_key_A[0]-1)
print("\nm =",m)
print("\nm =",hex(m))

c_A = encrypt(m, public_key_A[1], public_key_A[0])
print("\nc_A=",c_A)
print("\nc_A=",hex(c_A))
print("\n m =",decrypt(c_A, secret_key_A, public_key_A[0]))
print("\n m =",hex(decrypt(c_A, secret_key_A, public_key_A[0])))
if m == decrypt(c_A, secret_key_A, public_key_A[0]):
	print("yes")

c_B = encrypt(m, public_key_B[1], public_key_B[0])
print("\nc_B=",c_B)
print("\nc_B=",hex(c_B))
print("\n m =",decrypt(c_B, secret_key_B, public_key_B[0]))
print("\n m =",hex(decrypt(c_B, secret_key_B, public_key_B[0])))
if m == decrypt(c_B, secret_key_B, public_key_B[0]):
	print("yes")

sign_A = sign(m, secret_key_A, public_key_A[0])
print("\nsign_A =",sign_A)
print("\nsign_A =",hex(sign_A))

if verify(m,sign_A, public_key_A[1], public_key_A[0]):
	print("verifed")

sign_B = sign(m, secret_key_B, public_key_B[0])
print("\nsign_B =",sign_B)
print("\nsign_B =",hex(sign_B))

if verify(m,sign_B, public_key_B[1], public_key_B[0]):
	print("verifed")

k1, s1, s = send_key(k, public_key_B[1],  public_key_B[0],secret_key_A, public_key_A[0])
print("Abonent A have send key!")
print("k1 = ",k1)
print("s1 = ",s1)
print("Abonent B has received key!")

receive_key(k1,s1, secret_key_B, public_key_B[0], s, public_key_A[1], public_key_A[0])



k1, s1, s = send_key(k, int("10001", 16), int("AAE0EA1CF0CDE4B9D6B1E3F52514E33A28168C86557B14C36ACE527EC3851D7BEDD1FEC6130725F232CABC2ED06B5D73CF9ED3931564AF4E28C399CEA0779071", 16),secret_key_A, public_key_A[0])

print("k1 = ",hex(k1))
print("s1 = ",hex(s1))
print("s = ",hex(s))