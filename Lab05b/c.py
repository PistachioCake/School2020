# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  05b Program 3
# Date:        09 18 2020

# This program in one line:
# (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))(lambda f: lambda a, b, inp: f(b, a+b, int(input('Correct\n> '))) if inp == b else print('Incorrect'))(0, 1, int(input('> ')))

a, b = 0, 1
print('The first fibonnacci number is 0.')
while True:
	inp = int(input('What is the next fibonnacci number? > '))
	if inp == b: 
		print('Correct')
		a, b = b, a+b
	else: 
		print('Incorrect')
		break

