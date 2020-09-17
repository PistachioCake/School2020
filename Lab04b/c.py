# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  04b Program 3
# Date:        15 09 2020

# Reynold's Number: https://byjus.com/reynolds-number-formula
velocity = float(input('Velocity: '))
viscosity = float(input('Viscosity: '))
lin_dim = float(input('Linear Dimension: '))

reynolds_number = velocity * lin_dim / viscosity

kind = 'laminar'    if reynolds_number < 2000 else \
       'transition' if reynolds_number < 4000 else \
	   'turbulent'

print(f'The Reynold\'s Number for this fluid is {reynolds_number:.3f}, which is considered {kind}.')
