
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



# your code goes here



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
