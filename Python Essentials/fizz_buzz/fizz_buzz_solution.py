
# FizzBuzz Exercise
# =================
# 
# In this short exercise, we will program the core of a little game designed to teach children about the concept of divisibility. The idea is, for any given number, to print a special message if it is a multiple of 3 and/or 5, or else just print the number itself. It will teach you to use `if` statements to analyze that number as well as the modulo operator `%`. In the following lectures, we will learn about looping, which will be needed to draw and analyze more than 1 number at a time. For now, we will draw a number randomly and print the message for it.
# 
# The following code generates a random number from 1 to 100:


from random import randint
n = randint(1, 101)
print n


# Question 1
# ----------
# 
# For the first level of our game, write a test that prints "Fizz" if the number drawn is a multiple of 3, or just prints the number itself if it is not.
# 
# Test your code with many different values of `n` to make sure it works correctly. For that, run the code above again multiple times and you will see n taking multiple values. You can run your test after each generation of `n`. (That should make you look forward to learning about `for` loops :).)

# Hint: You can use the modulo operator to test for divisibility: `n` is divisible by 3 if `n % 3` equals 0.


if n % 3 == 0:
    print "Fizz"
else:
    print n


# Question 2
# ----------
# 
# The second level of our game will be a little more complex. Now write a test that prints "Fizz" if the number is a multiple of 3, or prints "Buzz" if the number is a multiple of 5.  If it is a multiple of both 3 and 5, it should print "FizzBuzz". Finally, if it is neither a multiple of 3 nor 5, it should just print the number.
# 
# Test your code with many different values of `n` to make sure it works correctly.


# There are multiple ways to solve this problem

# A straighforward way to do it is to make a case for each situation
if n % 3 == 0 and n % 5 == 0:
    print "FizzBuzz"
elif n % 5 == 0:
    print "Buzz"
elif n % 3 == 0:
    print "Fizz"
else:
    print n



# We could have solved this problem another way (not necessarily better nor worse, just different logic)
output = ""
if n % 3 == 0:
    output += "Fizz"
if n % 5 == 0:
    output += "Buzz"

if output != "":
    print output
else:
    print n


# Question 3
# ----------
# 
# We will be analyzing a lot of numbers. In real-life problems, the analyzing may be much more time consuming than just the modulo operation, so it would be useful to build a cache of the output text. What data structure would conveniently store a number and its corresponding message? Build an empty one called `cached_analysis`. In a separate cell, for a given number `n`, check if a message has already been stored. Print it if it has. Otherwise, use the same test as before to build the message, and store it in `cached_analysis` in addition to printing it.

# Hint: Since we want to map a number to a message, so that we can look up the number and print the corresponding message, the data-structure we need is a dictionary.


cached_analysis = {}



# A straightforward way to solve this:

if n in cached_analysis:
    print cached_analysis[n]
else:
    # Re-use the our testing form above but store the message in a variable instead of printing it
    # so that we don't have to repeat the message, once to print it and once to 
    if n % 3 == 0 and n % 5 == 0:
        msg = "FizzBuzz"
    elif n % 5 == 0:
        msg = "Buzz"
    elif n % 3 == 0:
        msg = "Fizz"
    else:
        msg = "%s" % n
    
    # Now store the message, mapping it to the number (since numbers are immutable) and print it
    cached_analysis[n] = msg
    print msg



# We could also architect the solution by checking first if the number is not in the dictionary 
# and building and storing the message for it.
# After that we can print the value corresponding to the number outside of the if statement.
# Take the time to look at this solution and make sure that you understand it.
if n not in cached_analysis:
    if n % 3 == 0 and n % 5 == 0:
        msg = "FizzBuzz"
    elif n % 5 == 0:
        msg = "Buzz"
    elif n % 3 == 0:
        msg = "Fizz"
    else:
        msg = "%s" % n

    cached_analysis[n] = msg

print cached_analysis[n]

# We thought of this solution by noticing that the straightforward solution above repeats the 
# instruction "print cached_analysis[n]" (or "print msg" which is equivalent) for both cases. 
# If that's the case, it means that there is a way to put that statement outside of the if 
# blocks. 

