# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  04b Program 4
# Date:        15 09 2020

from sympy import symbols
from sympy.solvers import solve

print('This program will solve a quadratic equation, given the coefficients.')

print('For an equation written as Ax**2 + Bx + C = 0, please input the coefficients.')
coeff_a = float(input('A: '))
coeff_b = float(input('B: '))
coeff_c = float(input('C: '))

x = symbols('x')
quadratic = coeff_a * x ** 2 + coeff_b * x + coeff_c
print('Solving:', quadratic)

solutions = solve(quadratic)
print('The solution(s) are:', ', '.join(f'{sol}' for sol in solutions))



