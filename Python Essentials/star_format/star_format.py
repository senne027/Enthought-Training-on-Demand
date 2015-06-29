
# Star Format Exercise
# ====================
# 
# The data file for the "Third Catalogue of Nearby Stars" contains information about nearby stars in lines which look like the following:
# 
# <pre>
# Proxima Centauri  M5  e      11.05 15.49 771.8
# Alp1Cen           G2 V        0.01  4.38 749.0
# Alp2Cen           K0 V        1.34  5.71 749.0
# 52Tau Cet         G8 Vp       3.49  5.77 286.0
# Eps Ret           K2 IV       4.44  3.57 067.0
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
# 
# These boundaries are both inclusive but include a space to the right of the value to separate it from the next. The apparent and absolute magnitude quantities have 2 decimal places of precision, while the parallax has 1. The parallax values should be padded with leading zeroes if the value is less than 100.
# 
# Question
# --------
# 
# Given the following values for a star, produce a properly formatted string using the `format` string method which would correspond to the last line of the file above. Store your response in a variable named `eps_ret`  and test your solution with the cell below.


star_name = "Eps Ret"
spectral_class = "K2 IV"
apparent_magnitude = 4.44
absolute_magnitude = 3.57
parallax = 67.0



# your code goes here



print eps_ret
success = eps_ret == "Eps Ret           K2 IV       4.44  3.57 067.0"
print("Is your solution valid? {0}".format(success))


# References
# ----------
# 
# <pre>
# Preliminary Version of the Third Catalogue of Nearby Stars
# GLIESE W., JAHREISS H.
# Astron. Rechen-Institut, Heidelberg (1991)
# </pre>
