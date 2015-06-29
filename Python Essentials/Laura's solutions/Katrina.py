#Code copied from katrina_advisory.py

f = open("katrina_advisory.txt")
text = f.read()
f.close()
print 'Content of "katrina_advisory.txt"'
print '-' * 51
print
print text

#1

text = text.lower()
text = text.strip()


alarming_terms =  (text.count("killed") + text.count ("destroyed") + text.count("death") + text.count("devastating"))

is_urgent = text.startswith("urgent") or text.startswith("URGENT")
print "Starts With Urgent?", is_urgent

danger_level = alarming_terms + (is_urgent*3)
print "Danger Level =", danger_level