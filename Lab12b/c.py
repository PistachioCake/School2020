# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  12b Program 3
# Date:        12 11 2020

import numpy as np
from matplotlib import pyplot as plt

array_m = np.array([[1.00583, -0.087256], [0.087156, 1.00583]])
array_v = np.array([[1, 0]])

plt.plot(*array_v[0], '.k')
for _ in range(250):
    array_v = array_v @ array_m
    plt.plot(*array_v[0], '.k')

plt.show()

