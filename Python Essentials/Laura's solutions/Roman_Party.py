friends = {'julius': '100 via apian', 'cleopatra': '000 pyramid parkway'}
romans = dict(brutus='234 via tratorium', cassius='111 aqueduct lane')
countrymen = dict([('plebius','786 via bunius'), ('plebia', '786 via bunius')])

print "Friends:", friends.keys()
print 'Addresses:', friends.values()
print "Friends and their Adresses:", friends.items()

#friends.pop([1])
del friends["julius"]

mail = {}

mail.update(friends)
mail.update(romans)
mail.update(countrymen)

print "Mailing List:", mail

print "Cleopatra's Address:", friends["cleopatra"]

mail.clear()
