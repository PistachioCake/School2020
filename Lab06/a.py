# By submitting this assignment, we agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "We have not given or received any unauthorized aid on this assignment"
# 
# Name:         Collin Stafford, Rushil Udani, Grant Trusty, Braeden Stewart
# Section:      219
# Assignment:   LAB 6 ASSIGNMENT
# Date:         04 October 2020

from math import sqrt

# Obtain input from the user and stores values in a list
trainer_vals = [input("Input the name of the Pokemon: "), int(input("Input the Pokemon's combat points (or CP): ")), 
		int(input("Input the Pokemon's current level: ")), int(input("Input the number of candies you currently have: "))]

# Prints the menu
print(trainer_vals[0])
print("Current CP:", trainer_vals[1])
print("Current Level:", trainer_vals[2])
print("Candies:", trainer_vals[3])
print("1 - Add Candy")
print("2 - Use Candy to Level-up")
print("3 - Exit to Main Menu")
print()

trainer_wants = int(input('What action will you do?: '))

while trainer_wants != 3:

	# Updates the Pokemon's candies if the user chooses #1
	if trainer_wants == 1:
		print()
		trainer_vals[3] += int(input('How many candies do you want to add?: ')) #
		# prints menu
		print(trainer_vals[0])
		print("Current CP:", trainer_vals[1])
		print("Current Level:", trainer_vals[2])
		print("Candies:", trainer_vals[3])
		print("1 - Add Candy")
		print("2 - Use Candy to Level-up")
		print("3 - Exit to Main Menu")
		print()
		trainer_wants = int(input('What action will you do?: '))

	# Updates the Pokemon's level if the user chooses #2
	elif trainer_wants == 2:
		print()
		if trainer_vals[2] < 30:
			trainer_vals[1] += trainer_vals[1] * 0.0094 / (0.095 * sqrt(trainer_vals[2])) ** 2 # cp increase
			trainer_vals[2] += 1 # level increase
			trainer_vals[3] -= 1 # candy decrease
		else:
			trainer_vals[1] += trainer_vals[1] * 0.0045 / (0.095 * sqrt(trainer_vals[2])) ** 2 # cp increase
			trainer_vals[2] += 1 # level increase
			trainer_vals[3] -= 2 # candiesy decrease
		# prints menu
		print(trainer_vals[0])
		print("Current CP:", trainer_vals[1])
		print("Current Level:", trainer_vals[2])
		print("Candies:", trainer_vals[3])
		print("1 - Add Candy")
		print("2 - Use Candy to Level-up")
		print("3 - Exit to Main Menu")
		print()
		trainer_wants = int(input('What action will you do?: '))
	else:
		print('Try again!')
		# If the input was invalid, the user gets an error message and the program ends
		trainer_wants = int(input('What action will you do?: '))

# Prints a thank you message when the user inputs a 3
print()
print("Thanks!")
