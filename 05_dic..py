'''
dict = {}
for i in range(1,5):
    dict[i] = i * 2
print(dict)

dictv2 = {i: i * 2 for i in range(1,5) }
print(dictv2)

import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries: 
    population[country] = random.randint(1,100)

print(population)
population = {country:random.randint(1,100) for country in countries}
print(population)
'''

name = ['nico', 'zule','santi']
age = [12,56,12]
print(list(zip(name,age)))

new_dict = {name : age for (name, age) in zip(name,age)}
print(new_dict)