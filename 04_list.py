'''
numbers = []

for element in range(1,11) : 
    numbers.append(element * 2)

print(numbers)


numbers_v2 = [e * 2  for e in range(1,11)]
print(numbers_v2)'''

numbers = []
for i in range(1,11) : 
    if i %2 == 0:
        numbers.append(i *2)
print(numbers)

numbersv2 = [i * 2 for i in range(1,11) if i %2 == 0]
print(numbersv2)
