# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  11b Program 4
# Date:        02 11 2020

from typing import List

def main(times: List[float], dists: List[float]):
	'''Input: Two parallel lists of times and the distance travelled by then.
	Output: The average velocity between consecutive time measurements.'''
	velocities = []
	for i in range(len(times) - 1):
		# velocity calculation: delta dist / delta time
		velocities.append((dists[i+1] - dists[i]) / (times[i+1] - times[i]))
	return velocities

while True:
	times = []
	dists = []
	print('This will repeatedly ask you to enter a time, and the distance at\n'
	      'that time. The times should be strictly increasing. Then, it should\n'
	      'tell you the average velocity within each time interval.\n')

	time = input('Enter time:\t')
	while time:
		times.append(float(time))
		dists.append(float(input('Enter distance:\t')))
		time = input('Enter time:\t')
	
	print()
	print('The velocities are:')
	print('\n'.join(str(v) for v in main(times, dists)))

	again = input('Would you like to test again? [y/n] ')
	if again.rstrip().lower().startswith('y'):
		continue
	else:
		print('Goodbye!')
		break

