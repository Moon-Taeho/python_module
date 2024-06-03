""" import my_module

result1 = my_module.add(10, 5)
print(result1)

result2 = my_module.subtract(10, 5)
print(result2)

result3 = my_module.introduce('Moon Taeho')
print(result3)

 """

from my_module import add, subtract, introduce

result1 = add(10, 5)
result2 = subtract(10, 5)
result3 = introduce('MOON TAEHO')

print(result1, result2, result3)

