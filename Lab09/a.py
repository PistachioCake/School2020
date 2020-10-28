# By submitting this assignment, We agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "We have not given or received any unauthorized aid on this assignment"

# Names:        Collin Stafford, Braeden Stewart, Rushil Udani, Grant Trusty
# Section:      219
# Assignment:   Lab 09 Assignment
# Date:         25 October 2020

# Get name of dependent variable
dvar_name = input('What is the name of the dependent variable?')

# Loop until 'q': Get x and y values
xvals = []
yvals = []

# Seed the loop
x = input('Input an x coordinate. Enter q to stop. ')

while x != 'q':
  x = float(x)

  # Make sure xvals is always in order
  i = 0
  while i < len(xvals) and xvals[i] < x:
    i += 1
  xvals.insert(i, float(x))
  
  # And that yvals is in the same order
  y = float(input('Input a corresponding y coordinate. '))
  yvals.insert(i, y)
    
  # Loop condition begins again here
  x = input('Input an x coordinate. Enter q to stop. ')

# Output data to file
with open('nailedIt.txt', 'w') as file:
  file.write('Team 4: Braeden Stewart, Grant Trusty, Rushil Udani, Collin Stafford\n')
  file.write('October 22, 2020\n')
  file.write('\n')
  file.write('x-values = time, y-values = ' + dvar_name + '\n')
  file.write('-----------------------------------------------------------------------\n')
  ind = 0
  for xnum in xvals:
    file.write('{:.6g}, {:.6g}\n'.format(xnum, yvals[ind]))
    ind += 1
  file.write('-----------------------------------------------------------------------\n')

print()
print('Enter x values to predict their corresponding y values:')

# Loop until 'q':
#   Get x-value from user
x = input('Input an x coordinate. Enter q to stop. ')
while x != 'q':
  x = float(x)
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
  if isExtrapolation: print('This was an extrapolation.')
  else: print('This was an interpolation.')
  
  # Output to file
  with open('nailedIt.txt', 'a') as file:
    coords = '{:.6g}, {:.6g}'.format(x, y) 
    if isExtrapolation: file.write('{:13s} extrapolation\n'.format(coords))
    else: file.write('{:13s} interpolation\n'.format(coords))

  x = input('Input an x coordinate. Enter q to stop. ')
