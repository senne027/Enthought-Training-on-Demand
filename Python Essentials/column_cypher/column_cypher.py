"""
Column Cypher
=============

A column cipher works by writing the message in rows of a fixed length, and
then extracting the columns and concatenating them.  So the message
"THISISACOLUMNCYPHER" with rows of length 5, would be written::

    THISI
    SACOL
    UMNCY
    PHERX

and then be sent as "TSUPHAMHICNESOCRILYX".  Note that you want to
pad the message with extra characters to make it a multiple of the number of
columns.

In this exercise you will encode the message "This message is very secret" with
a column cypher with rows of length 3.

1) It is common in these examples to remove spaces and use all upper-case
   letters.  Convert the message to this format with Python code.

2) Add a number of "X" characters to the end of the message so that its
   length is multiple of 3.

   Bonus: Try to do this so that if you change the message your code will still
   work.

   Hint: the modulo operator ``%`` gives the remainder when dividing by an
   integer.  What does ``%`` do to negative integers in Python?

3) The first column contains the characters at index 0, 3, 6, etc.  Use
   slices to extract this column.

4) Extract the second and third columns using slicing and produce the
   encoded message.

To decode the encoded message, you would repeat this process, but with 3
rows of length 8 instead of 8 rows of length 3.

Bonus
-----

If you know about functions and loops, you can attempt this bonus question.

5) Write a function which takes arguments of the message to encode and the
   number of rows

"""

message = "This message is very secret"

# 1) Remove spaces and convert to upper case

message = # your code goes here

print message

# 2) Pad the message with "X" characters to make the length an multiple of 3

padded_message = # your code goes here

print "Message:", padded_message

# 3) Extract the first column from the padded message.

column_0 = # your code goes here

# 4) Extract the second and third columns from the padded message and produce
#    the encoded message.

column_1 = # your code goes here

column_2 = # your code goes here

encoded_message = # your code goes here

print "Encoded:", encoded_message

# Bonus
# 5) Write a function that does this.

# your code goes here
