# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  06b Program 3
# Date:        30 09 2020

import matplotlib.pyplot as plt

n = int(input('Enter the starting number: '))
history = [n]
# Track the history of the

while n != 1:
	n = 3*n + 1 if n % 2 else n / 2
	history.append(n)

# range(len(history)) counts from 0 to len(history)
plt.plot(range(len(history)), history)
plt.show()

