red = 75
green = 0
blue = 130

indi = "#{red:02x}{green:02x}{blue:02x}".format(red=red, green=green, blue=blue)
print indi

indi_markdown = '<span style="color:{0:7s};">indigo</span>'.format(indi)
print indi_markdown