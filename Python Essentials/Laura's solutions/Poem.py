#Poem

poem = """
"Jack
Much to his Mum and Dad's dismay
Jack ate himself one day.
He didn't stop to say his grace,
He just sat down and ate his face.
"We can't have this his Dad declared,
"If that lad's ate, he should be shared."
But even as he spoke they saw
Jack eating more and more:
First his legs and then his thighs,
His arms, his nose, his hair, his eyes...
"Stop him someone!" Mother cried
"Those eyeballs would be better fried!"
"""

print poem.count("Jack")
print poem.find("Jack")

poem = poem.replace("Jack", "Horace")

print poem