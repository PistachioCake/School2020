# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  05b Program 2
# Date:        18 09 2020

print('\n'.join(f'{x} divides {y}' for y in range(2, 101) for x in range(2, y+1) if y % x == 0))
