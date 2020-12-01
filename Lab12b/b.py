# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  12b Program 2
# Date:        12 11 2020

import numpy as np
from matplotlib import pyplot as plt

START = 0
END = np.pi * 4
xvals = np.linspace(START, END, 144)
intersection_xvals = np.arange(np.pi / 4, END, np.pi)

y1vals = np.sin(xvals)
y2vals = np.cos(xvals)

intersection_yvals = np.sin(intersection_xvals)

fig, ax = plt.subplots()

# ls=(0,(9,3)) sets the linestyle to be 9 pt dashes with 3 pt spaces
ax.plot(xvals, y1vals, 'b', ls=(0,(9,3)))
ax.plot(xvals, y2vals, 'r-')
ax.plot(intersection_xvals, intersection_yvals, 'mo')

ax.set(xlabel='x values', ylabel='y values',
		title='Plot of cos(x) and sin(x)', )

plt.show()
