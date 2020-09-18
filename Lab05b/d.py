# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  05b Program 4
# Date:        18 09 2020

from sympy import Symbol, Eq, tan, cos, S, solveset, Interval, pi

DISTANCE = 202.3
ACCEL_G_EARTH = 9.8
ACCEL_G_MARS  = 3.72

vel_initial = float(input('What is Red\'s initial velocity? > '))

theta = Symbol('theta')

height_earth = DISTANCE * tan(theta) - ACCEL_G_EARTH * DISTANCE ** 2 / (2 * vel_initial ** 2 * cos(theta) ** 2)
height_mars  = DISTANCE * tan(theta) - ACCEL_G_MARS  * DISTANCE ** 2 / (2 * vel_initial ** 2 * cos(theta) ** 2)

solutions_earth = solveset(Eq(height_earth, 1), theta, domain=S.Reals).intersect(Interval(0, pi/2))
solutions_mars  = solveset(Eq(height_mars,  1), theta, domain=S.Reals).intersect(Interval(0, pi/2))

if solutions_earth:
	print('Earth:\t', float(list(solutions_earth)[0] * 180 / pi))
else:
	print('Earth:\t', 'No solution found')

if solutions_mars:
	print('Mars:\t', float(list(solutions_mars)[0] * 180 / pi))
else:
	print('Mars:\t', 'No solution found')

