
# Katrina Advisory Analysis
# =========================
# 
# We will keep analyzing the Katrina advisory report following the exercise from the string lecture where we computed a priority alert. Let's analyze it further by computing the number of words and paragraphs, and extracting its metadata. Let's assume that this is useful to know if our application will be able to post it on Twitter or send it by text messages or if other means of communication are needed.
# 
# Again, we will load the content of the advisory for you since we haven't seen how to read files yet.


f = open("katrina_advisory.txt")
text = f.read()
f.close()
print 'Content of "katrina_advisory.txt"'
print '-' * 51
print
print text


# Question 1
# ----------
# 
# Count the number of paragraphs in the text (2 paragraphs are delimited by a blank line). Print the result using  formating to obtain "The number of paragraphs is 12.".

# Hint: Paragraphs are delimited by the string "\n\n"


paragraphs = text.split("\n\n")
print("The number of paragraphs is {0}.".format(len(paragraphs)))


# Question 2
# ----------
# 
# Count the number of lines of text. This can be done without the need for a for loop, though a loop is an acceptable solution if you know how to implement it.

# Hint: How can we get a list of lines from the content of the file? Count the number of lines total. Count the number of empty lines. The result is 32.


lines = text.split("\n")
non_empty_lines = len(lines) - lines.count("")
print("There are %s lines in total, %s of which are not empty." 
      % (len(lines), non_empty_lines))


# Question 3
# ----------
# 
# We will define the first metadata for the alert message as a preview of the content. It will be made with the first 4 and the last 4 words. Combine this information  into a string type variable `preview` similar to `'The first four words ... the last four words'`.


words = text.split() 
preview = " ".join(words[:4]) + "..." + " ".join(words[-4:])


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


# Let's extract the first paragraph and store the rest in the 'content' variable
p1 = paragraphs[0]
content = "\n\n".join(paragraphs[1:])
# The priority is the first word
priority = p1.split()[0]
# Let's split the first paragraph into lines
p1_lines = p1.split("\n")
# The location will be whatever follows National Weather Service on the line 2
line2_words = p1_lines[1].split()
location = " ".join(line2_words[3:])
line3_words = lines[2].split()
time = " ".join(line3_words[:3])
date = " ".join(line3_words[3:])

print("Priority flag: {0}".format(priority))
print("Date: {0}".format(date))
print("Time: {0}".format(time))
print("Location: {0}".format(location))

