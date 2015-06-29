star_string = "Proxima Centauri  M5  e      11.05 15.49 771.8"

star_name = star_string[:18]
star_name = star_name.strip() #remove white space
spectral_class = star_string[18:28]
spectral_class = spectral_class.strip()
apparent_magnitude = float(star_string[29:34])
absolute_magnitude = float(star_string[35:40])
parallax = float(star_string[41:46])
#float numbers do not need the use of strip method

print "Star Name:", star_name
print "Spectral Class:", spectral_class
print "Apparent Magnitude:", apparent_magnitude
print "Absolute Magnitude:", absolute_magnitude
print "Parallax:", parallax
