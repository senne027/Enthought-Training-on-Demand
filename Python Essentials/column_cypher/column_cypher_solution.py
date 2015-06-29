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

message = message.replace(' ', '')
message = message.upper()

# 2) Pad the message with "X" characters to make the length an multiple of 3

padding = "X"

# Bonus: this works generally, but is a bit sneaky unless you know group theory
num_x = -len(message) % 3
padding = "X"*num_x

padded_message = message + padding

print "Message:", padded_message

# 3) Extract the first column from the padded message.

column_0 = padded_message[::3]

# 4) Extract the second and third columns from the padded message and produce
#    the encoded message.

column_1 = padded_message[1::3]

column_2 = padded_message[2::3]

encoded_message = column_0 + column_1 + column_2

print "Encoded:", encoded_message

# Bonus
# 5) Write a function that does this.

def encode_column(message, rows):
    """ Encode message using a column cypher with specified number of rows """
    message = message.replace(' ', '')
    message = message.upper()
    message += "X"*(-len(message) % rows)
    columns = [message[i::rows] for i in range(rows)]
    encoded_message = ''.join(columns)
    return encoded_message
