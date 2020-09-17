# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  04b Program 3 Challenge
# Date:        15 09 2020

# Reynold's Number: https://byjus.com/reynolds-number-formula
# More info also from: https://www.engineeringtoolbox.com/hydraulic-equivalent-diameter-d_458.html
# Viscosity information from: http://hyperphysics.phy-astr.gsu.edu/hbase/Tables/viscosity.html

viscosity_of_fluids = {
    '1': 0.01,        # Water
    '2': 0.00018,     # Air
    '3': 1.1,         # Oil (light)
	}

while True:
	fluid = input('Which fluid are you using?\n  [1] Water\n  [2] Air\n  [3] Oil\n\t> ')
	if fluid in viscosity_of_fluids:
		viscosity = viscosity_of_fluids[fluid]
		break
	else:
		print('Just type 1, 2, or 3 to pick a fluid.')
		continue

print(f'The fluid you chose is #{fluid}, with a viscosity of {viscosity}.')
	
velocity = float(input('Velocity (cm/s): '))
diameter = float(input('Diameter of pipe (cm): '))

reynolds_number = velocity * diameter / viscosity

kind = 'laminar'    if reynolds_number < 2000 else \
       'transition' if reynolds_number < 4000 else \
	   'turbulent'

print(f'The Reynold\'s Number for this fluid is {reynolds_number:.3f}, which is considered {kind}.')
