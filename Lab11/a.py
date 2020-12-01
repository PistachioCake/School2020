# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:	      Rushil Udani, Braeden Stewart, Collin Stafford, Grant Trusty
# Section:    219
# Assignment: Lab #11 Assignment 1
# Date:       5 / 11 / 2020
# ----------------------------------------- IMPORTS STATEMENTS------------------------------------------

import random
from math import radians, tan, cos, sin, dist
from matplotlib import pyplot as plt

# ---------------------------------------- FUNCTION DEFINITIONS-----------------------------------------
BIRDS = [
	# (name, color, size, description)
	('Red', 'red', .5, 'Red: red, small bird'), 
	('Chuck', 'yellow', .5, 'Chuck: yellow, small bird'), 
	('Bomb', 'black', 1, 'Bomb: black, large bird'), 
	('Terrence', 'red', 1, 'Terence: red, large bird'), 
        ]
PLANETS = [ # Description can be generated from the other two but this is easier
	# (name, gravity, description)
	('Earth', 9.807, 'Earth = 9.807 m/s^2'), 
	('Mars', 3.711, 'Mars = 3.711 m/s^2'), 
	('Moon', 1.625, 'Moon = 1.625 m/s^2'), 
	('Jupiter', 24.79, 'Jupiter = 24.79 m/s^2'), 
        ]

def get_basics():
	"""Takes user selections for active bird and planet. Returns (bird, planet). 'Bird' includes name,
	color and size. 'Planet' includes name and gravity. """
	a = bird_picker() # Runs fn to provide bird menu
	b = planet_picker() # Runs fn to provide planet menu
	return a, b[1]

def bird_picker():
	"""Takes user selection for bird. Returns (name, color, size). Gives a reprompting if an invalid option is entered."""
	print('Pick a bird:')
	for i, bird in enumerate(BIRDS):
		print('[{}]'.format(i+1), bird[-1])
	choice = int(input('\n >> ')) - 1

	while not 0 <= choice < len(BIRDS):
		print('Pick from one of the options above.')
		choice = int(input(' >> ')) - 1
		
	# Return the bird, without the description
	return BIRDS[choice][:-1]

def planet_picker():
	"""Takes user selection for planet. Returns (name, gravity). Gives a reprompting if an invalid option is entered."""
	print('Pick a Celestial Body:')
	for i, bird in enumerate(PLANETS):
		print('[{}]'.format(i+1), bird[-1])
	choice = int(input('\n >> ')) - 1

	while not 0 <= choice < len(PLANETS):
		print('Pick from one of the four options above.')
		choice = int(input('\n >> ')) - 1 

	return PLANETS[choice][:-1]

def get_guesses():
	"""Takes user guesses for velocity and launch angle. Returns (vel, angle)."""
	# Get velocity input
	vel = float(input("Input your guess for the initial velocity: "))
	# Get angle input (in degrees)
	angle = float(input("Input your guess for the launch angle in degrees: "))
	return vel, angle

def trajectory(g, vel, angle):
	xs = list(range(10, 1000, 10))
	ys = [trajectory_y(x, g, vel, angle) for x in xs]
	# Equivalent to:
	# ys = []
	# for x in xs:
	#     ys.append(trajectory_y(x, g, vel, angle))
	return xs, ys


def hit(xs, ys, target):
	target_x, target_y, target_size = target
	for i, x in enumerate(xs):
		y = ys[i]
		# ensure that `x` is at most `size` away from `target_x`
		# (Just to speed things up slightly)
		if not target_x - target_size < x < target_x + target_size:
			continue
		if dist((x, y), (target_x, target_y)) < target_size / 2:
			return True
	return False
	
def birds_plot(xs, ys, target, bird):
	fig, ax = plt.subplots(constrained_layout=True)
	ax.plot(xs, ys, c=bird[1], ls='--', lw=bird[2])
	circle = plt.Circle(target[0:2], target[2] / 2, color='green')
	ax.add_patch(circle)
	ax.set_aspect('equal')
	ax.set_xlim(0, None)
	ax.set_ylim(0, None)
	ax.plot() # Force an update
	if hit(xs, ys, target):
		# TODO: Draw x
		pass
	plt.show()

def trajectory_y(x, g, vel, angle):
	"""Returns (y-value) of the trajectory for a given x-value, gravity, initial velocity, and angle."""
	angle = radians(angle)
	return (x*tan(angle))-(g*x**2)/(2*(vel**2)*cos(angle)**2)

# -------------------------------------------- MAIN PROGRAM --------------------------------------------
# (Then your Main Program)
# Sets up loop so user can repeat the game as many times as desired ('y' to continue, 'n' to quit)
pig_counter = 0
again = 'y'
while again == 'y':

	# Program will pick a random distance (x from 10-1000), height (y from 0-50) and size of a target
	target = (random.randint(10, 1000), random.randint(0, 50), random.randint(10, 50))

	# Takes initial guesses
	bird, g = get_basics()                # Runs fn to get bird and planet information
	v_guess, theta_guess = get_guesses()  # Runs fn to get initial velocity and angle guesses

	# Loops guesses until bird hits target
	x, y = trajectory(g, v_guess, theta_guess)      # Create current x- and y- value lists
	while not hit(x, y, target):                    # Program cycles until throw hits the target
		birds_plot(x, y, target, bird)              # Plots trajectory & target of miss
		v_guess, theta_guess = get_guesses()        # Gets updated guesses from user
		x, y = trajectory(g, v_guess, theta_guess)	# Creates updated lists of x- and y-values
		
	# Handles winning case and asks if user would like to play again
	print('Yay!')
	pig_counter += 1
	birds_plot(x, y, target, bird)
	again = input('Would you like to play again? (y/n) ')
	while again not in {'y', 'n'}:
		again = input('Please type either y or n only. Would you like to play again? (y/n) ')
		
# Exiting when user decides to quit
print('\nThanks for playing! You popped {} pig(s) today!'.format(pig_counter))
