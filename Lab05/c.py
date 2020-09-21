# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani, Braeden Stewart, Grant Trusty, Collin Stafford
# Section:     219
# Assignment:  05 Program 2 and 3
# Date:        21 09 2020
import numpy
import matplotlib.pyplot as plt
from sys import exit

# Test Cases:
#  A | B |  C | D | left | right | sol
#  1 | 0 |  0 | 0 | -4   | 1     | 0
#  1 | 0 | -4 | 0 |  1   | 4     | 2
# -1 | 2 | -3 | 4 |  0   | 2     | 1.650629
#  0 | 1 |  2 | 1 | -3   | 0     | not found

print('This program will solve a cubic equation, given the coefficients, and a bound on the solution.')

# ----------- User Input --------------
print('For an equation written as A*x**3 + B*x**2 + C*x + D = 0, please input the coefficients.')
coeff_a = float(input('A: '))
coeff_b = float(input('B: '))
coeff_c = float(input('C: '))
coeff_d = float(input('D: '))
print()

print('The left bound must be less than the right, and they must contain exactly one single root.')

left = float(input('left  bound: '))
right = float(input('right bound: '))

print(f'Solving: {coeff_a}*x**3 + {coeff_b}*x**2 + {coeff_c}*x + {coeff_d} = 0, over the domain x ∈ [a, b]')

f = lambda x: coeff_a * x ** 3 + coeff_b * x ** 2 + coeff_c * x + coeff_d

# Check if this range is increasing or decreasing
# We can simplify some future logic using this
if f(left) < 0 and f(right) > 0:
    inc = True
elif f(right) < 0 and f(left) > 0:
    inc = False
elif f(left) == 0:
    print(f'Solution: {left:.6f}, after 0 iterations.')
    exit(0)
elif f(right) == 0:
    print(f'Solution: {right:.6f}, after 0 iterations.')
    exit(0)
else:
    print('Cannot find root if bounds are the same sign.')
    exit(1)

# ------------ Solving ----------------
iterations = 0

while abs(left - right) > 1e-6:
    iterations += 1
    # Binary search over [a, b]
    new = (left + right) / 2
    if (f(new) > 0) ^ inc:
        left = new
    else:
        right = new

print(f'Solution: {left:.6f}, after {iterations} iterations.')

# Create x-values for plot
lower_range_val = float(input('What is the lower bound of the graph?: '))
upper_range_val = float(input('What is the upper bound of the graph?: '))
xvals = numpy.arange(lower_range_val, upper_range_val, 0.01)  # Values with 0.01 spacing from bounds a to b

yvals = coeff_a * xvals ** 3 + \
        coeff_b * xvals ** 2 + \
        coeff_c * xvals + coeff_d  # Evaluate function at every point defined by xvals.

plt.plot(xvals, yvals)  # Create line plot with yvals against xvals
plt.show()  # Show the figure
