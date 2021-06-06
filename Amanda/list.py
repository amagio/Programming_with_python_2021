cities_lived = ['Montreal', 'San Francisco', 'Austin']
populations = [500, 700, 800]
cities = [cities_lived, populations]
number_of_cities = len(cities_lived)
#if number_of_cities <= 10:
   # for i in range(0, number_of_cities):
       # print(cities_lived[i])


for i in range(0, number_of_cities):
    print(cities[0][i], 'has a population', cities[1][i])



