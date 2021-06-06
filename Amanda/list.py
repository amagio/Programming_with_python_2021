cities_lived = ['Montreal', 'San Francisco', 'Austin']
populations = [500, 700, 800]
cities = [cities_lived, populations]

number_of_cities = len(cities_lived)

if number_of_cities <= 10:
   for i in range(0, number_of_cities):
       print(cities_lived[i])

print('\n')


for i in range(0, number_of_cities):
    print(cities[0][i], 'has a population', cities[1][i])

print('\n')

cities_dict = {}

for i in range(number_of_cities):
    cities_dict[cities[0][i]] = [cities[1][i]]

print(cities_dict)

print('\n')

for i , j in cities_dict.items():
    print('city of', i , 'has a population of', j)
