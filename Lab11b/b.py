# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  11b Program 2
# Date:        02 11 2020

from statistics import mean
from typing import List, Tuple

def main(values: List[float]) -> Tuple[float, float, float]:
	'''Input: a list of float values. Output: the minimum, mean and maximum of these'''
	return min(values), mean(values), max(values)

# Test the function
while True:
	values = []
	print('This will repeatedly ask you to enter values for a list. Leave the\n'
	      'name empty to stop inputting. Then, it should tell you the minimum,\n'
		  'mean, and maximum values of that list.\n')

	value = input('Enter value:\t')
	while value:
		values.append(float(value))
		value = input('Enter value:\t')
	
	print()
	result = main(values)
	print('Min:\t{}\nMean:\t{}\nMax:\t{}'.format(*result))

	again = input('Would you like to test again? [y/n] ')
	if again.rstrip().lower().startswith('y'):
		continue
	else:
		print('Goodbye!')
		break

