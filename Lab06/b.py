# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani, Grant Trusty, Braeden Stewart, Collin Stafford
# Section:     219
# Assignment:  06 Program 2
# Date:        01 10 2020

import matplotlib.pyplot as plt

# ------------ Part 1: Creating the data ------------------

fuel_cost = float(input('What is the price of fuel [$/gal]?\n\t> '))
distance = float(input('What is the distance of the trip [miles]?\n\t> '))

mph_list = []
mpg_list = []
cost_list = []
time_list = []

for speed in range(5, 85, 5): # Speeds from 5 to 80 in 5 mph_list increments
	mph_list.append(speed)
	mpg = -5.9852 + 1.6052 * speed - 0.0141 * speed**2
	mpg_list.append(mpg)
	cost_list.append(distance / mpg * fuel_cost)
	time_list.append(distance / speed)

print()

# ------------ Part 2: Using the data ---------------------

menu = '''
What would you like to do?
[1] Create a table displaying MPH, MPG, Cost, and Travel time
[2] Create a plot of speed (25-80 mph) vs. cost
[3] Create a plot of cost vs. travel time (25-80 mph)
[4] Calculate the cost and time at a specific speed
[5] Calculate the minimum cost and speed to make the distance in a given time
[6] Quit
\t> '''

while True:
	option = input(menu)
	while option not in set('123456'):
		print('Not a valid option.\n\n')
		option = input(menu)
	option = int(option)
	
	if option == 1:
		# [1] Create a table displaying MPH, MPG, Cost, and Travel time
		print(f'{"MPH": >7} | {"MPG": >7} | {"cost [$]": >7} | {"time [hr]": >7}')
		print('-'*8 + '|' + '-'*9 + '|' + '-'*9 + '|' + '-'*8)
	
		for i in range(len(mph_list)):
			print(f'{mph_list[i]: >7} | {mpg_list[i]: >7.2f} | {cost_list[i]: >7.2f} | {time_list[i]: >7.2f}')
	elif option == 2:
		# [2] Create a plot of speed (25-80 mph) vs. cost
		plt.plot(mph_list[4:], cost_list[4:])
		plt.xlabel('Speed [mph]')
		plt.ylabel('Cost [$]')
		plt.show()
	elif option == 3:
		# [3] Create a plot of cost vs. travel time (25-80 mph)
		plt.plot(cost_list[4:], time_list[4:])
		plt.xlabel('Cost [$]')
		plt.ylabel('Time [hours]')
		plt.show()
	elif option == 4:
		# [4] Calculate the cost and time at a specific speed
		speed = float(input('What speed do you want to calculate [mph]?\n\t> '))
		mpg = -5.9852 + 1.6052 * speed - 0.0141 * speed**2
		cost = distance / mpg * fuel_cost
		time = distance / speed
		print(f'{"MPH": >7} | {"MPG": >7} | {"cost [$]": >7} | {"time [hr]": >7}')
		print(f'{speed: >7} | {mpg: >7.2f} | {cost: >7.2f} | {time: >7.2f}')
	elif option == 5:
		# [5] Calculate the minimum cost and speed to make the distance in a given time
		time_max = float(input('What is the time limit to use?\n\t> '))

		# Accumulate all data in one list for easy manipulation
		data = zip(mph_list, mpg_list, cost_list, time_list)
		# Remove all data points that take too long
		data = list(filter(lambda d: d[3] < time_max, data))

		if not data:
			print('No calculated speed fulfilled this time minimum.')
			continue

		# Calculate minimum speed and cost for the remaining data values
		min_speed = min(data, key=lambda d:d[0])
		min_cost = min(data, key=lambda d:d[2])

		print(f'The minimum speed is achieved at {min_speed[0]} mph, with a cost of ${min_speed[2]:.2f}')
		print(f'The minimum cost  is achieved at {min_cost[0]} mph, with a cost of ${min_cost[2]:.2f}')
	else:
		# [6] Quit
		print('Quitting.')
		break
	
