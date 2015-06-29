f = open("katrina_advisory.txt")
text = f.read()
f.close()
print 'Content of "katrina_advisory.txt"'
print '-' * 51
print
print text

paragraphs = text.split("\n\n")
print("The number of paragraphs is {0}.".format(len(paragraphs)))

lines = text.split("\n")
non_empty_lines = len(lines) - lines.count("")
print("There are %s lines in total, %s of which are not empty." 
      % (len(lines), non_empty_lines))
      

words = text.split() 
preview = " ".join(words[:4]) + "..." + " ".join(words[-4:])

print words

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


print""
print("Priority flag: {0}".format(priority))
print("Date: {0}".format(date))
print("Time: {0}".format(time))
print("Location: {0}".format(location))