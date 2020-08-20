# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  01b
# Date:        27 08 2020

from math import sin, cos

print('This shows the function (sin x)/x evaluated close to x=0')
for x in map(lambda x: 10**(-x), range(6)):
	print(sin(x)/x)
print()

print('This shows the function (1 - cos x) / x^2 evaluated close to x=0')
for x in map(lambda x: 10**(-x), range(6)):
	print((1 - cos(x)) / x ** 2)
print()

print('This shows the function (1 + 1/x)^x evaluated close to x=infinity')
for x in map(lambda x: 10**x, range(6)):
	print((1 + 1/x) ** x)
