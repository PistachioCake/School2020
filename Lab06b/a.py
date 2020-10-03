# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  06b Program 1
# Date:        30 09 2020

measurements = [15.80, 19.60, 21.85, 33.61, 49.73, 51.27, 56.26, 63.06, 76.56,
		76.57, 85.78, 90.74, 92.60, 99.71,100.51, 101.12, 101.25, 102.19, 
		104.85, 110.59, 125.92, 131.25, 136.04, 141.15, 148.54, 150.02]

measurements.append(162.76)

measurements.insert(8, 71.01)

print(f'There were {len(measurements)} days of data measurements taken.')
print('-'*50)

# Split measurements into 4 groups of 7
weeks = [measurements[7*i:7*i+7] for i in range(4)]

def mean(l): return sum(l)/len(l)
def avg_daily_growth(l): return (l[-1] - l[0])/(len(l)-1)
# This would be used if only the avg daily growth for the week
# weren't so weirdly calculated

for i, week in enumerate(weeks):
	print(f'Average moss mass in week {i+1}: {mean(week): >12.2f} g')

print('-'*50)

for i in range(4):
	# Like seriously what is this, why is the first day of the next week being used?
	# I mean I get it but then we need the 29th day's data to keep it consistent
	print(f'Average daily growth during week {i+1}: {(measurements[min(len(measurements)-1, 7*i+7)] - measurements[7*i])/7: >5.2f} g/day')

print('-'*50)

print(f'Average growth for the month: {avg_daily_growth(measurements): >11.2f} g/day')
