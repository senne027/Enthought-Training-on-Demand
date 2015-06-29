
# Prime Numbers
# =============
# 
# Background
# ----------
# 
# A [prime number](http://en.wikipedia.org/wiki/Prime_number) is a number that has no divisors other than 1 and itself. For example, 4 is not a prime number because it can be evenly divided by 2 (4 divided by 2 is an integer, 2), while 5 is a prime number because it cannot be divided by 2, 3, or 4.
# 
# A classic algorithm to find primes is the [Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).
# Prime numbers have various interesting applications, including cryptography, for example in the widely used 
# [RSA encryption](http://en.wikipedia.org/wiki/RSA_%28cryptosystem%29) algorithm.
# 
# The goal of this short exercise is to get toward a reasonably efficient way to collect all prime numbers that are below one million.
# The exercise will get you to experiment with nested `for` loops, both breaking out of them, as well as the `for-else` construct, a pattern that is a little more advanced than the basic `for` loop but that is very convenient in certain situations.
# 
# To efficiently check very many numbers for being prime, we will want to be a little clever in how many tests we do. For example, when we are testing if 5 is prime, we can actually skip testing if it is divisible by 4. Since 4 is not a prime number, as it equals 2 times 2, if 4 is a divisor then 2 must be as well. So if we have already checked for divisibility by 2, then we can skip checking for divisibility by 4.
# In fact, we really only need to test for division by prime numbers. More optimizations than this are possible as well.
# 
# Question 1
# ----------
# 
# For the first step, let's write some code to test if a single number, say 79, is a prime number.

# Hint: If you don't know where to start, try to encode the reasoning we followed above for testing if 5 was a prime number. Also remember that `x % y` equals 0 if `y` evenly divides `x`. Finally, the `for-else` pattern can be useful here to detect that we have tried unsuccessfully to divide 79 by all possible divisor candidates.


# your code goes here


# Question 2
# ----------
# 
# Reuse the code above to create a list containing all prime numbers less than `max_n=100`.  Print the length of the list.


# your code goes here


# Bonus
# -----
# 
# In Python, `for` loops are slower than in C or Fortran, especially for very large numbers of items. For most common operations, where the number of items in the loop is modest, Python is fast enough. But if you deal with a very long list of objects, and especially if you use nested loops, like in our algorithm above, the looping can become quite slow. 
# 
# To observe this, run the code above with increasing `max_n`, up to 1000, 10000, or even higher if you are patient, and notice how the execution time goes from instantaneous to many seconds.
# 
# One of the main reasons that loops can be slow, is that Python can have arbitrary types of objects in a list, which makes some optimizations difficult to apply. This is one of the main reasons for the existence of the [Numpy](http://www.numpy.org/) module and tools like [Cython](http://www.cython.org/) that we will cover later in other courses. 
# 
# If we want to find all the primes less than 1000000, we will need to be careful about our algorithm, and avoid too much looping. Think about some ways to skip some of the values in our nested loops above. For help, have a look to http://en.wikipedia.org/wiki/Prime_number or open the hint below.

# Hint: There are a couple of simple optimizations that we can use.
# 
# First, since all prime numbers except 2 are odd, we can start by taking 2 as prime and then only checking odd numbers starting with 3.
# 
# Second, we only actually need to check for prime factors up to, and including, the square root of the number we are testing. If the test number is divisible by something larger than the square root, then the resulting quotient must be less than the square root, and we would find that as a divisor first. This is an especially important optimization for large numbers.


# your code goes here

