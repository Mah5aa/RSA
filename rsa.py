from decimal import Decimal 
from time import time
from timeit import default_timer as timer
import random
import math
from textwrap import wrap
from sympy import *

inputMsg = input("Enter ur msg: ")

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def gcd(m,n): 
    if n==0: 
        return m 
    else: 
        return gcd(n,m%n) 

#input variables
#p = 213695557 #int(input("enter p:"))
#q = 268166761 #int(input("enter q:"))
primes=[]

for i in range(int(math.sqrt(2)*math.pow(2,27)),int(math.pow(2,28))): #28 bit p,q (√2⋅2n/2−1,2n/2) 
    if (isprime(i)):
        primes.append(i)

##print("primes:",primes)
p = random.choice(primes)
q = random.choice(primes)
while gcd(p,q)!=1:
    q = random.choice(primes)

#print("p:",p)
#print("q:",q)

startkey=timer()
#calculate n
n = p*q 
#calculate Phi_n
Phi_n = (p-1)*(q-1) 
#calculate e
for e in range(2,Phi_n): 
    if gcd(e,Phi_n)== 1: 
        break

d=modinv(e, Phi_n)
#for i in range(1,100000000000000000): 
#    x = 1 + i*Phi_n 
#    if pow(x,1,e) == 0: 
#        d = int(x/e) 
#        break

public = (e,n)
private = (d,n)
Endkey=timer()
executionkey=Endkey-startkey

def split16bit(m):
    #print("m:",m)
    while len(m)%8!=0:
        m+=' '
    x=[]
    z=""
    for i in range(0,len(m)):
        subm=m[i:i+1]
        asci=ord(subm)
        if asci>=100:
            asci-=100
            if asci<10:
                tmp='0'+str(asci)
            else:
                tmp=''+str(asci)
        else:
            tmp=''+str(asci)
        z+=str(tmp)
    
    #print("z:",z)
    x=wrap(z, 16) #spli 16bit
    return x

def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    y=split16bit(n_text)
    for i in range(0,len(y)):
            #m= ord(i)
            c=pow(int(y[i]),e,n)
            x.append(c)
    return x 

def decrypt(priv_key,c_text):
    d,n=priv_key
    x=''
    m=0
    for i in c_text:
        # m=((int(i)**d))%n
        m = pow(int(i),d,n)
        tmp=''+str(m)
        if len(tmp)!=16:
            tmp='0'+tmp
        #print("m:",m)
        #print("tmp:",tmp)
        z=wrap(tmp, 2)
        for i in range(0,len(z)):
            asci=int(z[i])
            if asci>=0 and asci<=22:
                asci+=100
            c=chr(asci)
            x+=c
    return x

print("p:",p)
print("q:",q)
print('n = '+str(n))
print('Phi_n = '+str(Phi_n))
print('e = '+str(e))   
print('d = '+str(d))
print('Key Generation Time = ', executionkey) 
enc = encrypt(public,inputMsg)
startenc=timer()
print ("encrypted: " , encrypt(public,inputMsg))
endenc=timer()
execenc=endenc-startenc
startdec=timer()
print ("decrypted: " , decrypt(private,enc))
enddec=timer()
execdec=enddec-startdec
print("RSA Encryption Time:",execenc)
print("RSA Decryption Time:",execdec)