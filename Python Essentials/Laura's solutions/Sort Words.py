speech = '''Four score and seven years ago our fathers brought forth
         on this continent a new nation, conceived in Liberty, and
         dedicated to the proposition that all men are created equal.
         '''

speech = speech.lower()
speech = speech.replace(".", " ")
words = speech.split()

words.sort()

print "All words, in alphabetical order:"
print words
print ""
print "The first 2 words: "
print words[:2]
print ""
print "The last 2 words: "
print words[-2:] 