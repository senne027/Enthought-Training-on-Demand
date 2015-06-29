
# Star Data Exercise
# ==================
# 
# The data file for the "Third Catalogue of Nearby Stars" contains information about nearby stars in lines which look like the following:
# 
# <pre>
# Proxima Centauri  M5  e      11.05 15.49 771.8
# Alp1Cen           G2 V        0.01  4.38 749.0
# Alp2Cen           K0 V        1.34  5.71 749.0
# 52Tau Cet         G8 Vp       3.49  5.77 286.0
# </pre>
# 
# The data is provided in fixed-width fields, as follows:
# 
# <pre>
#  0:17   Star name
# 18:28   Spectral class
# 29:34   Apparent magnitude
# 35:40   Absolute magnitude
# 41:46   Parallax in thousandths of an arc second
# </pre>
# Both the lower limit and in the upper limit are inclusive here.
# 
# Given the following string, containing one line from the file, extract each of the data items from the string.  You should strip extraneous whitespace and convert strings containing floating point numbers to Python floats.


star_string = "Proxima Centauri  M5  e      11.05 15.49 771.8"



# The slicing will extract the part of the string that is relevant. Since 
# slicing in python is not inclusive on the upper limit, it is 18 instead of
# 17:
star_name = star_string[:18]
# Then we remove the white spaces:
star_name = star_name.strip()
# To be more compact, and if it is as readable to you, feel free to do both 
# steps at once:
spectral_class = star_string[18:28].strip()
# Since the float function deals with white spaces, the call to .strip is not needed in the next 3 lines:
apparent_magnitude = float(star_string[29:34])
absolute_magnitude = float(star_string[35:40])
parallax = float(star_string[41:46])



print "Star name:         ", star_name
print "Spectral class:    ", spectral_class
print "Apparent magnitude:", apparent_magnitude
print "Absolute magnitude:", absolute_magnitude
print "Parallax:          ", parallax


# References
# ----------
# 
# <pre>
# Preliminary Version of the Third Catalogue of Nearby Stars
# GLIESE W., JAHREISS H.
# Astron. Rechen-Institut, Heidelberg (1991)
# </pre>
