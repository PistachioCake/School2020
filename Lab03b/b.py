# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  03b Program 2
# Date:        09 10 2020

from math import hypot

def color_blue(s):
	return f'\u001b[38;5;69m{s}\u001b[0m'

def color_red(s):
	return f'\u001b[38;5;196m{s}\u001b[0m'


mass = 2.8

x1 = float(input(color_blue('Red\'s x position for the first point:') + '\t > '))
y1 = float(input(color_blue('Red\'s y position for the first point:') + '\t > '))
t1 = float(input(color_blue('The time of the first point:          ') + '\t > '))
print()
x2 = float(input(color_blue('Red\'s x position for the second point:') + '\t > '))
y2 = float(input(color_blue('Red\'s y position for the second point:') + '\t > '))
t2 = float(input(color_blue('The time of the second point:          ') + '\t > '))
print()

vel_x = (x2 - x1) / (t2 - t1)
vel_y = (y2 - y1) / (t2 - t1)
vel_composite = hypot(vel_x, vel_y)

kinetic_energy = 1/2 * mass * vel_composite ** 2

print(color_red('Red\'s kinetic energy is approximately'),
		f'{kinetic_energy:.3f}', color_red('joules.'))

