star_name = "Eps Ret"
spectral_class = "K2 IV"
apparent_magnitude = 4.44
absolute_magnitude = 3.57
parallax = 67.0

star_format = "{0:17s} {1:10s} {2:>5.2f} {3:>5.2f} {4:0>5.1f}"
eps_ret = star_format.format(star_name, spectral_class, apparent_magnitude,
                             absolute_magnitude, parallax)



print eps_ret
success = eps_ret == "Eps Ret           K2 IV       4.44  3.57 067.0"
print("Is your solution valid? {0}".format(success))