#1

#To create a list, always use brackets

employee_emails = ["Wile.E.Coyote@acme.com", 
 "Looney.Tunes@acme.com", 
 "Chuck.Jones@acme.com", 
 "Road.Runner@acme.com", 
 "Michael.Maltese@acme.com",
 "Speedy.Gonzales@acme.com",
 "Calamity.Coyote@acme.com",
 "Bugs.Bunny@texavery.com"]
 
IDs = range(8)
 
employee_emails.append("Acceleratti.incredibilis@acme.com")
IDs.append(8)

print employee_emails[2:6]

print employee_emails[::2]

employee_emails.remove('Looney.Tunes@acme.com')
IDs.pop(1)

acme_locations = ["Taos", "Phoenix", "Santa Fe", "Flagstaff"]

acme_locations.reverse()
print acme_locations


acme_locations = acme_locations[::-1]
print acme_locations