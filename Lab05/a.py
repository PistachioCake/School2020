# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani, Grant Trusty, Braeden Stewart, Collin Stafford
# Section:     219
# Assignment:  05 Program 1
# Date:        25 09 2020

# We have 10 seconds and 500 feet to accelerate to 88 mph

TIME_LIMIT = 10
DIST_LIMIT = 500

accel = float(input('What\'s the acceleration [ft/s^2]? '))

TIME_STEP = 0.1

velocity = 0
dist = 0
iterations = 0

while velocity < 88:
	iterations += 1
	velocity = accel * time * 5280 / 3600
	time = iterations * TIME_STEP
	dist = 1/2 * accel * time ** 2
	if time > TIME_LIMIT:
		print('Marty, this acceleration is too small to achieve\n'
		      'the required speed with the given constraints.\n'
			 f'You will only reach {velocity:.3f} mph before I update.')
		break
	if dist > DIST_LIMIT:
		print('Marty, this acceleration is too small to achieve\n'
		      'the required speed with the given constraints.\n'
			 f'You will only reach {velocity:.3f} mph before the road ends.')
		break
else:
	print('You made it!\n'
	     f'It took {time:.1f} seconds to accelerate to 88 mph.')

print(f'This calculation took {iterations // 120} banana peels.')

