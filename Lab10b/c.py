# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  10b Program 3
# Date:        28 10 2020

from matplotlib import pyplot as plt
from csv import DictReader

filename = input('Name for CSV File: ')
# Read file and get data
months = []
principals = []
with open(filename + '.csv', 'r') as fileh:
	filereader = DictReader(fileh)
	for line in filereader:
		months.append(int(line['Month']))
		principals.append(float(line['Principal Balance']))
	# If the loan balance is decreasing, the final balance should be 0.
	if principals[0] > principals[1]:
		months.append(months[-1] + 1)
		principals.append(0)


fig, ax = plt.subplots()

ax.plot(months, principals, 'ob')

ax.set(xlabel='Month', ylabel='Principal Balance',
		title='Amortization Schedule', )
ax.grid()

plt.show()

