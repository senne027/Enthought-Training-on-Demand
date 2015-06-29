#1

flight_distances = {frozenset(['Atlanta', 'Chicago']): 590, 
                    frozenset(['Atlanta', 'Dallas']): 720}

#2

flight_distances = {
    frozenset(['Atlanta', 'Chicago']): 590.0,
    frozenset(['Atlanta', 'Dallas']): 720.0,
    frozenset(['Atlanta', 'Houston']): 700.0,
    frozenset(['Atlanta', 'New York']): 750.0,
    frozenset(['Austin', 'Dallas']): 180.0,
    frozenset(['Austin', 'Houston']): 150.0,
    frozenset(['Boston', 'Chicago']): 850.0,
    frozenset(['Boston', 'Miami']): 1260.0,
    frozenset(['Boston', 'New York']): 190.0,
    frozenset(['Chicago', 'Denver']): 920.0,
    frozenset(['Chicago', 'Houston']): 940.0,
    frozenset(['Chicago', 'Los Angeles']): 1740.0,
    frozenset(['Chicago', 'New York']): 710.0,
    frozenset(['Chicago', 'Seattle']): 1730.0,
    frozenset(['Dallas', 'Denver']): 660.0,
    frozenset(['Dallas', 'Los Angeles']): 1240.0,
    frozenset(['Dallas', 'New York']): 1370.0,
    frozenset(['Denver', 'Los Angeles']): 830.0,
    frozenset(['Denver', 'New York']): 1630.0,
    frozenset(['Denver', 'Seattle']): 1020.0,
    frozenset(['Houston', 'Los Angeles']): 1370.0,
    frozenset(['Houston', 'Miami']): 970.0,
    frozenset(['Houston', 'San Francisco']): 1640.0,
    frozenset(['Los Angeles', 'New York']): 2450.0,
    frozenset(['Los Angeles', 'San Francisco']): 350.0,
    frozenset(['Los Angeles', 'Seattle']): 960.0,
    frozenset(['Miami', 'New York']): 1090.0,
    frozenset(['New York', 'San Francisco']): 2570.0,
    frozenset(['San Francisco', 'Seattle']): 680.0,
}


print "Distance between Seattle and Chicago:", flight_distances[frozenset(["Chicago", "Seattle"])]

# Compute the total distance flying from Austin to Houston to San Francisco and compare it to the distance if you fly Austin to Dallas to Los Angeles to San Francisco.
flight_1 = flight_distances[frozenset(["Austin", "Houston"])] + flight_distances[frozenset(["Houston", "San Francisco"])]
flight_2 = flight_distances[frozenset(["Austin", "Dallas"])] + flight_distances[frozenset(["Dallas", "Los Angeles"])] + flight_distances[frozenset(["Los Angeles", "San Francisco"])]

print "The flight 1 has", flight_1, "miles"
print "The flight 2 has", flight_2, "miles"

flight_distances[frozenset(['Austin', 'San Francisco'])] = 1500

del flight_distances[frozenset(['Boston', 'Miami'])]

flying_circus_cities = ['Houston', 'Chicago', 'Miami', 'Boston', 'Dallas', 'Denver', 'New York', 
                        'Los Angeles', 'San Francisco', 'Atlanta', 'Seattle', 'Austin']
southby_cities = ['Chicago',  'Los Angeles', 'New York', 'Boston', 'Orlando', 'Dallas', 
                  'Toronto', 'Denver', 'Miami', 'San Francisco', 'Houston', 'Atlanta', 'Seattle', 
                  'Vancouver']
                  
#1

merger_cities = set(flying_circus_cities)
merger_cities.update(southby_cities)                  
print "Number of cities that would be reached by the merger:", len(merger_cities)

#2
print "Cities that Flying Circus is contributing to the merger:", set(flying_circus_cities) - set(southby_cities)

# 3
print "Cities that Flying Circus doesn't reach that the merger will:", set(southby_cities) - set(flying_circus_cities)

# 4. That is what the symmetric difference provides: the list of elements in one of the sets but not both:
print "Number of cities reached once:", len(set(flying_circus_cities) ^ set(southby_cities))

#Another way to do it
#print "Number of cities reached once:", len(merger_cities) - len(set(flying_circus_cities) & set(southby_cities))

