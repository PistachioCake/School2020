# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  07b Program 2
# Date:        06 10 2020

from math import sin

f = lambda x: sin(x) / (sin(x/10) + x/10)

lower = float(input('Lower bound: '))
upper = float(input('Upper bound: '))

values = []
for i in range(11):
	try:
		x = lower + (upper - lower) * i / 10
		values.append(f(x))
		# Alternatively, values.append(sin(x) / (sin(x/10) + x/10))
		print(f'At x={x: >5.2f}, f(x) = {f(x): >5.2f}')
	except ZeroDivisionError:
		values.append(None)
		print(f'At x={x: >5.2f}, f(x) divides by zero')

print(f'The maximum value was {max(v for v in values if v is not None):.2f}')
