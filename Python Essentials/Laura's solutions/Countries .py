countries = open("NCDC_country_list.txt", "r").read()

# Let's normalize the content
countries = countries.lower()
print countries

country_list = countries.strip().split("\n")

b_countries = [country for country in country_list if country[0] == "b"]
b_countries = [country for country in countries.split("\n") if country.startswith("b")]


s_countries = [country for country in country_list if country[0] == "s"]
s_countries = [country for country in countries.split("\n") if country.startswith("s")]

print""
print "Countries that start with the letter B:", b_countries
print""
print "Countries that start with the letter S:", s_countries #why is it also showing countries that are country[0]=="l"???

unique_b = set(b_countries)
print "Countries starting with letter B:", unique_b
print""
unique_s = set(s_countries)
print "Countries starting with letter S:",unique_s