# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani, Braeden Stewart, Collin Stafford, Grant Trusty
# Section:     219
# Assignment:  09 Program 1
# Date:        17 10 2020

from matplotlib import pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
from math import exp

# fig is the figure, ax1 and ax2 are the two axes systems - i.e. the two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False, sharey=False, constrained_layout=True, num='Frodo likes this.')

# =========== DATA VALUES =============

t_vals = [0, 0.45, 1.1, 1.75, 2.25, 2.7]
y_vals = [0, 0.23, 0.4, 0.18, 0.07, 0.01]

# Calculate data points for the two functions
ts = []
y1 = []
y2 = []

for i in range(50):
	t = 3 * i / 50
	ts.append(t)
	y1.append(t**2 * exp(-t**2))
	y2.append(t**4 * exp(-t**2))

# =========== AXIS 1 ==================

# We want the scale to be [0, 3) - i.e. not show the 3, so we set xlim[1] to just under 3
ax1.set(xlabel='time', ylabel='y', title='Data and two curves vs. time', xlim=(0, 3-1e-8), ylim=(-0.05, 1.05))

# fmt ok => large black circles
ax1.plot(t_vals, y_vals, 'ok', label='data')

ax1.plot(ts, y1, '-r', label=r't^2*exp(-t^2)')
ax1.plot(ts, y2, '-b', label=r't^4*exp(-t^2)')

ax1.legend()

# =========== AXIS 2 ==================
ax2.set(xlabel='time', ylabel='y', title='Data interpolation and Curve 1', xlim=(1, 2), ylim=(0, 0.5))

# We split this up so the legend does not have a line
ax2.plot(t_vals, y_vals, '^y', label='data')
ax2.plot(t_vals, y_vals, '-y')

ax2.plot(ts, y1, '-b', label=r't^2*exp(-t^2)')

ax2.annotate('It\'s closest here!', xy=(1.405, 0.275), xytext=(-80, -50), 
             xycoords='data', textcoords='offset pixels',
             fontsize=10, arrowprops={'arrowstyle':'-|>'})

ax2.legend()

plt.show()
