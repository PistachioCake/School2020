# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  11b Program 1
# Date:        02 11 2020

from typing import List

def main(names: List[str], costs: List[float], values: List[float]) -> str:
	'''Input: three parallel lists of names (str), costs (float), and values 
	(floats). Ouptut: the name of the factory with the least profit'''
	# Get name of factory with minimum profit
	min_profit = values[0] - costs[0]
	min_name = names[0]
	for i, name in enumerate(names):
		profit = values[i] - costs[i]
		if profit < min_profit:
			min_profit = profit
			min_name = name

	return min_name

	# More concisely:
	# factories = zip(names, costs, values)
	# return min(factories, key=lambda factory:factory[2]-factory[1])[0]

# Test the function
while True:
	names  = []
	costs  = []
	values = []
	print('This will repeatedly ask you to enter the name of a factory, the\n'
	      'annual cost to operate it, and the value of the products produced\n'
	      'there. Leave the name blank to stop inputting. Then, it should tell\n'
	      'you the name of the least profitable factory of this list.\n')

	name = input('Enter name:\t')
	while name:
		names.append(name)
		costs.append(float(input('Enter cost:\t')))
		values.append(float(input('Enter value:\t')))
		name = input('Enter name:\t')
	
	print()
	print(main(names, costs, values))

	again = input('Would you like to test again? [y/n] ')
	if again.rstrip().lower().startswith('y'):
		continue
	else:
		print('Goodbye!')
		break
