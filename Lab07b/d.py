# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  07b Program 4
# Date:        06 10 2020

letter_to_points = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0, 'U':0}

n = int(input('How many classes are you taking this semester? '))

courses = []
for _ in range(n):
	print()
	name = input('What is the name of this course? ')
	hours = int(input('How many credit hours is this couse? '))
	grade = input('What is the final letter grade in this course? ').strip().upper()
	courses.append((name, hours, grade))

total_hours = 0
total_points = 0

for (name, hours, grade) in courses:
	total_hours += hours
	total_points += letter_to_points.get(grade, 0) * hours

gpa = total_points / total_hours

print()
print('Your gpa is {:.3f}'.format(gpa))

