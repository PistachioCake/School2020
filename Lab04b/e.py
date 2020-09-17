# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  04b Program 5
# Date:        16 09 2020

# ==== Estimated Points ==============+
points = [                          # |
  (0,    0   , 'Origin')            # |
, (0.01, 42.5, 'Linear Elastic')    # |
, (0.01, 42.5, 'Ignored')           # |
, (0.06, 42.5, 'Plastic')           # |
, (0.18, 60  , 'Strain Hardening')  # |
, (0.26, 50  , 'Necking') ]         # |
# ==== End Points ====================+


# Get user input and ensure it is in the correct domain. 
while True:
	try:
		user_strain = float(input('Please input a strain value: '))
	except ValueError:
		print('Make sure this is formatted as a number.\n')
		continue
	
	if 0 <= user_strain <= 0.26:
		break
	else:
		print('This model only has data between a strain of 0 and 0.26.\n')

# Get points that bound the region of the model user_strain is
for (strain, stress, reg), (prev_strain, prev_stress, _) in zip(points[1:], points):
	if user_strain <= strain:
		strain1, stress1 = prev_strain, prev_stress
		strain2, stress2 = strain,      stress
		region = reg
		break
else:
	# Should never happen, because we already did bounds checking above.
	print('Could not calculate!')

# Linear Interpolation
slope = (stress2 - stress1) / (strain2 - strain1)
calc_stress = slope * (user_strain - strain1) + stress1

# Output
print(f'Predicted stress: {calc_stress:.3f}, and this point is in the {region} region.')

