lyrics = '''My Bonnie lies over the ocean.
            My Bonnie lies over the sea.
            My Bonnie lies over the ocean.
            Oh bring back my Bonnie to me.
         '''
         
lyrics = lyrics.lower()

lyrics = lyrics.replace('.','')

words = lyrics.split()

o_words = []

for word in words:
    if word[0] == "o":
        o_words.append(word)
print o_words    

#why do I have to use print set(o_words) if this script works? 