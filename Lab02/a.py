# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani, Collin Stafford, Braeden Stewart, Grant Trusty
# Section:     219
# Assignment:  02b
# Date:        03 09 2020

from math import pi

time_1 = 30			# seconds
measurement_1 = 50	# meters
time_2 = 45
measurement_2 = 615


def main():
	measurement_check_1 = compute_measurement(37)
	print(measurement_check_1, 'meters at 37 seconds')
	measurement_check_2 = compute_measurement(60 * 20) # 20 minutes
	print(measurement_check_2, 'meters at 20 minutes')


def compute_measurement(time_check):
	"""Given a time to check for, use linear interpolation
	   and extrapolation to calculate the measurement at that point
	   in time."""
	speed = (measurement_2 - measurement_1) / (time_2 - time_1)
	measurement_check = measurement_1 + (time_check - time_1) * speed
	measurement_check %= pi * 1000 # Circle with radius 0.5 km

	return measurement_check


if __name__ == '__main__':
	main()
	
