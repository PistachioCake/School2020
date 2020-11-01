# By submitting this assignment, I agree to the following:
#	"Aggies do not lie, cheat, or steal, or tolerate those who do"
#	"I have not given or received any unauthorized aid on this assignment"
#
# Names:			 Rushil Udani, Grant Trusty, Braeden Stewart, Collin Stafford
# Section:		 219
# Assignment:	10 Program 1
# Date:				29 10 2020

from matplotlib import pyplot as plt

# ========== Load data from file ============= #

filename = input('Name for input file (default nailedIt): ') or 'nailedIt'

with open(filename + '.txt', 'r') as fileh:
	fileh.readline() # Team names
	fileh.readline() # Date
	fileh.readline() # Empty

	var_names = fileh.readline().strip().split(sep=', ')
	x_var_name = var_names[0][11:]
	y_var_name = var_names[1][11:]

	fileh.readline() # Dashes

	xvals = []
	yvals = []
	line = fileh.readline()				 # [x val], [y val]
	while not line.startswith('-'):
		values = line.split(', ')
		xvals.append(int(values[0]))
		yvals.append(int(values[1]))
		line = fileh.readline()


# ======== Predict y from user supplied x ========== #

# Get x-value from user
x = float(input('Input an x coordinate: '))
# Find containing region
# Get index of right bounding point
i = 0
while i < len(xvals) and xvals[i] < x:
	i += 1
	# Calculate y-value from region
if i == 0: # Extrapolation to the left
	# Same formula as interpolation in the first region
	i = 1
	isExtrapolation = True
elif i == len(xvals): # Extrapolation to the right
	# Same formula as extrapolation in the last region
	i -= 1
	isExtrapolation = True
else:
	isExtrapolation = False
left_x = xvals[i-1]
right_x = xvals[i]
left_y = yvals[i-1]
right_y = yvals[i]
slope = (right_y - left_y)/(right_x - left_x)
y = slope * (x - left_x) + left_y
print('The x value {:.6g} corresponds to the y value {:.6g}'.format(x, y))
if isExtrapolation: 
	print('This was an extrapolation.')
else:
	print('This was an interpolation.')

# =============== Graph data and point ========== #

fig, ax = plt.subplots()

ax.set(xlabel=x_var_name, ylabel=y_var_name, 
		title=y_var_name + ' vs. ' + x_var_name)

# 'o--k' is a dashed black line with large circles
ax.plot(xvals, yvals, 'o--k', label=y_var_name)

# (40, 40) was chosen arbitrarily
ax.annotate('Your data point\ny={:.2f}'.format(y), xy=(x, y), xytext=(40, 40),
		xycoords='data', textcoords='offset pixels',
		fontsize=10, arrowprops={'arrowstyle':'->'})

# Save and reset the ylim to prevent autorescaling
ylim = ax.get_ylim()
ax.plot([x, x], [ylim[0], y], '--g')
ax.set_ylim(ylim)

# 'ob' is large blue circles
ax.plot(x, y, 'ob')

ax.legend()

plt.show()
