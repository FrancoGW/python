set_country = {'col','mex','bol'}
print(set_country)
print(type(set_country))

set_numbers = {1,2,3,4,5,6}
print(set_numbers)

set_types = {1,'hola',False,12.21}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuples = set(('abc','cvd' , 'dc', 'abc'))
print(set_from_tuples)


numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)

print(set_numbers)

unique_numbers = list(set_numbers)
print(unique_numbers)