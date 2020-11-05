# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  11b Program 3
# Date:        02 11 2020

def main(i: int) -> bool:
	'''Input: A positive integer. Output: whether the integer is perfect.'''
	divisors = get_all_divisors(num)
	return sum(divisors) == num

def get_all_divisors(num):
	# Return all proper divisors of num
	return [i for i in range(1, num) if num % i == 0]

	# The code following uses only that which we have learned
	# The above is more efficient, so I'm using that.

	# divisors = []

	# # Include 1, don't include num
	# for i in range(1, num):
	# 	if i % num == 0:
	# 		divisors.append(i)
	# return divisors

while True:
	print('This program will repeatedly get a number, then should output whether\n'
	      'it is a perfect integer or not.\n')

	num = int(input('Enter a number: '))
	if main(num):
		print(f'{num} is a perfect number.')
	else:
		print(f'{num} is not a perfect number.')

	again = input('Would you like to test again? [y/n] ')
	if again.rstrip().lower().startswith('y'):
		continue
	else:
		print('Goodbye!')
		break
