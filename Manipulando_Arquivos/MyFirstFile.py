with open("primeiro.txt", "a") as arquivo:
    arquivo.write("\nMeu primeiro arquivo segunda linha")

'''>>> from geopy.distance import geodesic
>>> newport_ri = (41.49008, -71.312796)
>>> cleveland_oh = (41.499498, -81.695391)
>>> print(geodesic(newport_ri, cleveland_oh).miles)
538.390445368
Using great-circle distance, also taking pair of (lat, lon) tuples:

>>> from geopy.distance import great_circle
>>> newport_ri = (41.49008, -71.312796)
>>> cleveland_oh = (41.499498, -81.695391)
>>> print(great_circle(newport_ri, cleveland_oh).miles)
536.997990696'''