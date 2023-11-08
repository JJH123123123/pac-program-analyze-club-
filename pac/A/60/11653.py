import math 

n = int(input())
sqrtn = math.ceil(math.sqrt(n))

# isprime
isprime = True

for i in range(2,sqrtn+1):
    if n % i == 0:
        isprime = False
        break

if(isprime or n ==1):
    if(n==1):
        exit(0)

    print(n)
    exit(0)

for i in range(2,sqrtn+1):
    while(n%i==0):
        print(i)
        n//=i

    if(n==1):
        break

if(n!=1):
    print(n)