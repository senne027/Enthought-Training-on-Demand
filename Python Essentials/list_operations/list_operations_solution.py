
# List Operations
# ===============
# 
# This exercise provides the opportunity to experiment some more with list creation and the use of their methods. Feel free to skip.
# 
# Create a list 'a' with the elements 10,21,23,11 and 24 in this order


a = [10,21,23,11,24]


# Modify the first element and the last element to be 0.


a[0] = 0
a[-1] = 0


# The following questions can all be answered using the appropriate methods attached to the list a.
# 
# Add the element 11 at the end of the list a.

# Hint: To explore the available methods, type a.< TAB > in  ipython.


a.append(11)


# How many occurrences of 11 is there in a?


a.count(11)


# Extend the list a with another list ["foo",4]


a.extend(["foo",4])


# What is the location of the first occurrence of 11?


a.index(11)


# Insert the value 100 as the third element. 

# Hint: All python sequences start at index 0. 


a.insert(2,100)


# Remove the forth element.

# Hint: All python sequences start at index 0. 


a.pop(3)


# Remove the first occurrence of 11


a.remove(11)


# Sort the list


a.sort()


# Reverse the list


a.reverse()


# Compute the length of the resulting list. 


l = len(a)


# Test if 11 is in the list anymore and if 99 is *not* in the list


print 11 in a
print 99 not in a

