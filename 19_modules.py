import sys

print(sys.path)

import re 

text = ' mi numero de telefono es 1222233, el codigo del pais es 57, mi numero de la suerte es el 3'

result = re.findall('[0-9]+',text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result= time.asctime(local)
print(timestamp)
print(result)

import collections

numbers = [1,1,2,1,2,1,4,5,3,3,21]

counter = collections.Counter(numbers)
print(counter)