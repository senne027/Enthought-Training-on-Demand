
# Managing ACME
# =============
# 
# Question 1
# ----------
# We are now (badly) managing the employees of a new startup called [ACME Corp.](http://en.wikipedia.org/wiki/Acme_Corporation), which has locations in Taos, Phoenix, Santa Fe, and Flagstaff. The employees of this company have the following email addresses (by order of arrival date in the company):
# <pre>
# "Wile.E.Coyote@acme.com", 
# "Looney.Tunes@acme.com", 
# "Chuck.Jones@acme.com", 
# "Road.Runner@acme.com", 
# "Michael.Maltese@acme.com",
# "Speedy.Gonzales@acme.com",
# "Calamity.Coyote@acme.com",
# "Bugs.Bunny@texavery.com"
# </pre>
# 
# Copy these 8 emails into a list called `employee_emails`. Also create a list of employee IDs from 0 to 7 without writing each ID manually (let's assume that we will reuse your code once ACME's products finally start to work and sell and the company becomes huge). 


employee_emails = ["Wile.E.Coyote@acme.com", 
                   "Looney.Tunes@acme.com", 
                   "Chuck.Jones@acme.com", 
                   "Road.Runner@acme.com", 
                   "Michael.Maltese@acme.com", 
                   "Speedy.Gonzales@acme.com",
                   "Calamity.Coyote@acme.com", 
                   "Bugs.Bunny@texavery.com"]
employee_ids = range(8)


# Question 2
# ----------
# A new employee, number 8, is joining the company: "Acceleratti incredibilis". Add his email address to the list. Update the employee_ids list.


employee_emails.append("Acceleratti.incredibilis@acme.com")
employee_ids.append(8)


# Question 3
# ----------
# Suprisingly, one of ACME's products, the "Earthquake Pills" work remarkably well and were developed surprisingly fast. Pull up the emails for the team responsible for them, that is employees with IDs 2, 3, 4 and 5. This can be done using slicing.


print employee_emails[2:6]


# Question 4
# ----------
# Despite the Earthquake Pills, this year, the poor financial results of the company only allow to pay bonuses to every other employee (starting with employee 0). Using slicing, pull up their email addresses to announce the good news to them. (Once we learn about NumPy and SciPy, we will learn to select employees based on their performances rather than arrival dates!)


print employee_emails[::2]


# Question 5
# ----------
# If fact the following year, the company is doing even worse. Mad not to have had a bonus the year before the Looney Tunes decides to spin off half the company to create a new one with employees with odd IDs, except that Bugs Bunny guy (employee 7), because he doesn't really belong here... Pull up their emails to send them a secret message.

# Hint: Again slicing could help here since we can extract every other element with it. Could we change the start point to grab the other set of every other employee?


# The odd employees (no pun intended) can be collected by selecting a slice 
# that has a step of 2 and a start of 1 instead of starting from the beginning.
employee_emails[1:7:2]


# Question 6
# ----------
# His communication was intercepted: Looney Tunes is fired. Remove him from the list of employees. Remove his employee ID as well. 


# We can remove values using either the remove or the pop methods. 
employee_emails.remove('Looney.Tunes@acme.com')
employee_ids.pop(1)


# Question 7
# ----------
# Capture the list of locations of the company in a list (ordered by importance): "Taos", "Phoenix", "Santa Fe", and "Flagstaff". Considering the management issues in ACME, it is decided to reverse the order of these locations, and move the headquarters to Flagstaff. Update the list of locations.


acme_locations = ["Taos", "Phoenix", "Santa Fe", "Flagstaff"]
# Remember that reverse is an inplace operation so 
# acme_locations = acme_locations.reverse()
# would give surprising results. Try it out if you want and check the value of 
# acme_locations. We will understand that once we learn about functions. 
acme_locations.reverse()
print acme_locations


# Question 8
# ----------
# The Boss ends up missing the nice skiing in Taos, and decides to reverse the location order again. The challenge here is to reverse the order without using the reverse method.

# Hint: Slicing could help...


# Slicing can help here because the step can be negative: -1 goes backwards though the list.
acme_locations = acme_locations[::-1]
print acme_locations

