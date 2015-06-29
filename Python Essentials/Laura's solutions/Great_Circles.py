from math import sin, cos, asin, radians    

def haversine_formula(r, p1, p2):
    phi_1, lambda_1 = p1
    phi_2, lambda_2 = p2
    
    phi_1 = radians(phi_1)
    phi_2 = radians(phi_2)
    lambda_1 = radians(lambda_1)
    lambda_2 = radians(lambda_2)
    
# $a = \sin^{2}(\Delta \phi/2) + \cos(\phi_{1})\cos(\phi_{2})\sin^{2}(\Delta \lambda/2)$
# 
# $c = 2 \arcsin(\sqrt{a})$
# 
# $d = rc$
# 
# Where $\phi_{i}$ is latitude and $\lambda_{i}$ is the longitude of point $i$ and $r$ is the radius of the globe.

    a = sin((phi_1-phi_2)/2)**2 + cos(phi_1)*cos(phi_2)*sin((lambda_1-lambda_2)/2.0)**2
    c = 2*asin(a**0.5)
    return r*c
    

#script to test the answer: 

r_earth = 6371.0 # km
austin = (30.2500, -97.7500)
cambridge = (52.2050, 0.1190)

print round(haversine_formula(r_earth, austin, cambridge))


cities = {
    'Atlanta': (33.7569444444, -84.3902777778),
    'Austin': (30.3, -97.7333333333),
    'Boston': (42.3577777778, -71.0616666667),
    'Chicago': (41.9, -87.65),
    'Dallas': (32.7825, -96.7975),
    'Denver': (39.7391666667, -104.984722222),
    'Houston': (29.7627777778, -95.3830555556),
    'Los Angeles': (34.05, -118.25),
    'Miami': (25.7833333333, -80.2166666667),
    'New York': (40.67, -73.94),
    'San Francisco': (37.7666666667, -122.433333333),
    'Seattle': (47.6, -122.316666667),
}


def distances(cities, city_1, city_2):
    r_earth = 6371.0 # km
    distance = haversine_formula(r_earth, cities[city_1], cities[city_2])
    return round(distance, -1)
    
print distances(cities, 'Austin', 'San Francisco')

def compute_distances(cities):
    r_earth = 6371.0 # km
    
    distances = {}
    unvisited = set(cities)
    for city_1 in cities:
        unvisited.remove(city_1)
        
        location_1 = cities[city_1]
        for city_2 in unvisited:
            location_2 = cities[city_2]
            distance = haversine_formula(r_earth, location_1, location_2)
            distances[frozenset((city_1, city_2))] = round(distance, -1)
            
    return distances



compute_distances(cities)
