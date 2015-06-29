votes = "y y n N Y Y n n N y Y n Y"

votes = votes.upper()

yes = votes.count("Y")
no = votes.count("N")

total = yes+no

print "Vote percentage:"

print "% yes:", yes/float(total)*100

print "%no:", no/float(total)*100
