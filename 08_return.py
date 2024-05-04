def sum_with_ragne(a,b):
    sum = 0
    for x in range(a, b):
        sum += x
    return sum

result = sum_with_ragne(1,10)
print(result)
result_v2 = sum_with_ragne(result,result + 10)
print(result_v2)

