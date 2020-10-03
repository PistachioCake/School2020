# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  06b Program 2
# Date:        30 09 2020

inputs = []
# Loop until break
while True:
	user_in = input('Enter an integer, or \'q\' to quit: ')
	if user_in == 'q':
		break
	try:
		user_in = int(user_in)
		# Only add even integers to the list
		if user_in % 2 == 0: inputs.append(user_in)
	except ValueError:
		print('Not a valid integer')

print(sorted(inputs))

