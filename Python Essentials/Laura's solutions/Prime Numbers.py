x = 79
for n in range(2, x):
    if x % n == 0:
        print x, "is not a prime number"
        break
else:
    print x, "is a prime number"
    

max_n = 100
primes = []

for n in range(2, max_n):
    for p in primes:
        if n % p == 0:
            break
   #could I add a 'not' and use 'continue' instead?
   
    else:
        
        primes.append(n)

print "There are {0} primes less than {1}".format(len(primes), max_n)

max_n = 1000000
primes = [2]


for n in range(3, max_n, 2):
    max_p = int(n**0.5)
    for p in primes:
        if n % p == 0:
            break
        elif p > max_p:
            primes.append(n)
            break

print "There are {0} primes less than {1}".format(len(primes), max_n)

