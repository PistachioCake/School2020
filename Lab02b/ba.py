# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  02b Program 2a
# Date:        09 03 2020

time_1 = 13
pos_1 = (1, 3, 7)
time_2 = 84
pos_2 = (23, -5, 10)

time_check = 50

def main():
	pos_new = (
	  compute_measurement(time_1, pos_1[0], time_2, pos_2[0], time_check), 
	  compute_measurement(time_1, pos_1[1], time_2, pos_2[1], time_check), 
	  compute_measurement(time_1, pos_1[2], time_2, pos_2[2], time_check), 
	  )

	print(f"Time of interest: {time_check} seconds\n"
		  f"x0 = {pos_new[0]} m\n"
		  f"y0 = {pos_new[1]} m\n"
		  f"z0 = {pos_new[2]} m\n")

def compute_measurement(time_1, measurement_1, time_2, measurement_2, time_check):
	"""Given a time to check for, use linear interpolation
	   and extrapolation to calculate the measurement at that point
	   in time."""
	speed = (measurement_2 - measurement_1) / (time_2 - time_1)
	measurement_check = measurement_1 + (time_check - time_1) * speed

	return measurement_check


if __name__ == '__main__':
	main()
	
