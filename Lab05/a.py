# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani, Grant Trusty, Braeden Stewart, Collin Stafford
# Section:     219
# Assignment:  05 Program 1
# Date:        25 09 2020

# We have 10 seconds and 500 feet to accelerate to 88 mph

# ------------ Problem-Specific Constants -------------------------------------
TIME_LIMIT = 10
DIST_LIMIT = 500
TIME_STEP = 0.1

# ------------ User input ----------------------------------------------------- 
accel = float(input('What\'s the acceleration [ft/s^2]? '))
print()

# ------------ Calculations ---------------------------------------------------
dist = 0
iterations = 0
velocity = 0

while velocity < 88:
	iterations += 1
	# Calculate current time and distance based on how many iterations we've gone through
	time = iterations * TIME_STEP
	dist = 1/2 * accel * time ** 2
	# Get velocity in mph
	velocity = accel * time * 5280 / 3600

	# Check if we've exceeded our boundaries
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
else: # If we didn't break, meaning we didn't pass the time or distance bounds
	print('You made it!\n'
	     f'It took {time:.1f} seconds to accelerate to 88 mph.')

print(f'This calculation took {iterations // 120} banana peels.')

