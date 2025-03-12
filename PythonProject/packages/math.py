from addition import add
from addition.add import addition
from addition.subtraction.diff import difference
from addition.subtraction.multiply import multi
from addition.subtraction.multiply.multi import multiply
from addition.subtraction.multiply.divide import division
from addition.subtraction.multiply.divide.division import divide

sum = addition(5, 6)
print('Sum of given numbers is : ',  sum)

name = "John"
age = 30

print("Name :", name)


minus = difference(6, 8)
print(minus)

product = multiply(4, 5)
print(product)


mul = multi.multiply(6, 7)
print(mul)


div = division.divide(5, 75)
print(div)

div1 = divide(4, 64)
print(div1)
