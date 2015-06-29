"""
Caesar Cypher
=============

A Caesar cypher is a simple substitution cypher where each letter is replaced
by the letter shifted some fixed distance down the alphabet, wrapping around
when you reach Z.

So for example if the shift is 3, then:

    A -> D
    B -> E
    C -> F
    ...
    X -> A
    Y -> B
    Z -> C

In this exercise you will encode and decode text in a Caesar cypher.

1) Use slicing and string concatenation to build a string with the upper case
   letters shifted by 10.

2) Look at the documentation for the `translate` method on strings and the
   `maketrans` function from the `string` module (which we have imported for
   you).

   Use the `translate` method and `maketrans` to encode the string
   "HELLO WORLD" with the letters shifted by 10.

3) The variable `secret_message` contains a message which has been encoded
   using a shift of 10.  Decode it.

Bonus
-----

4) If you know about functions write a function that takes a message and a shift
   and produces the encoded message.  Make sure that you support both positive
   and negative shifts, as well as shifts greater than 26.

"""

from string import maketrans

# 1) create a string with the letters shifted by 10

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

shifted_letters = # your code goes here

# 2) use `maketrans` and the `translate` method to encode this string

message = "HELLO WORLD"

encoded_message = # your code goes here

print encoded_message

# 3) decode this message which has been encoded by this cypher

secret_message = "ZIDRYX SC KGOCYWO"

decoded_message = # your code goes here

print decoded_message

# Bonus
# 4) write a function which encodes a message

# your code goes here
