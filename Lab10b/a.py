# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  10b Program 1
# Date:        27 10 2020

with open('Celsius.dat', 'r') as celsius_in:
	with open('Farenheit.dat', 'w') as farenheit_out:
		for celsius in celsius_in:
			farenheit_out.write(str(float(celsius.strip()) * 9 / 5 + 32) + '\n')
