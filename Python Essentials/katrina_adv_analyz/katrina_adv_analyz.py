
# Katrina Advisory Analysis
# =========================
# 
# We will keep analyzing the Katrina advisory report following the exercise from the string lecture where we computed a priority alert. Let's analyze it further by computing the number of words and paragraphs, and extracting its metadata. Let's assume that this is useful to know if our application will be able to post it on Twitter or send it by text messages or if other means of communication are needed.
# 
# Again, we will load the content of the advisory for you since we haven't seen how to read files yet.


# your code goes here


# Question 1
# ----------
# 
# Count the number of paragraphs in the text (2 paragraphs are delimited by a blank line). Print the result using  formating to obtain "The number of paragraphs is 12.".

# Hint: Paragraphs are delimited by the string "\n\n"


# your code goes here


# Question 2
# ----------
# 
# Count the number of lines of text. This can be done without the need for a for loop, though a loop is an acceptable solution if you know how to implement it.

# Hint: How can we get a list of lines from the content of the file? Count the number of lines total. Count the number of empty lines. The result is 32.


# your code goes here


# Question 3
# ----------
# 
# We will define the first metadata for the alert message as a preview of the content. It will be made with the first 4 and the last 4 words. Combine this information  into a string type variable `preview` similar to `'The first four words ... the last four words'`.


# your code goes here


# Question 4
# ----------
# 
# Let's analyze the first paragraph and normalize its content:
# <pre>
# URGENT — WEATHER MESSAGE
# NATIONAL WEATHER SERVICE NEW ORLEANS LA
# 1011 AM CDT SUN AUG 28, 2005
# </pre>
# 
# Parse it to extract its priority flag made of the first word of the paragraph, the location it originates from (city, state), the time and the date and store that into 4 distinct variables. It is safe to assume that the location will always follow "National Weather Service" on the second line and that the time will always be the first 3 entries on the third line. 
# 
# Store the rest of the message into a "content" variable.
# 
# These date, location and flag metadata could be used add this information automatically on a map, in a calendar, with appropriate flagging, though this is beyond the scope of this exercise. 


# your code goes here

