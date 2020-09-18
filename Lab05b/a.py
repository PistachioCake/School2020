# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  05b Program 1
# Date:        18 09 2020

import sys

first = float(input('Enter a measurement: '))

if first < 0:
	print('No measurements were processed.')
	sys.exit(0)

count = 1
avg = min = max = first
while (measurement := float(input('Enter a measurement: '))) > 0:
	if measurement < min: min = measurement
	if measurement > max: max = measurement
	avg = (avg * count + measurement) / (count + 1)
	count += 1

print('From these measurements:\n'
     f'The average is {avg}\n'
	 f'The minimum is {min}\n'
	 f'The maximum is {max}\n'
	 )
