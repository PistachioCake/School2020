# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  09b Program 2
# Date:        19 10 2020

print('This program surveys the students in a class.')
print('Enter a negative age to stop inputting data.')


males = []
females = []

while True:
	age = int(input('Enter the student\'s age: '))
	if age < 0:
		break
	gender = input('Enter the student\'s gender [m/f]: ')[0].lower()
	if gender == 'm':
		males.append(age)
	elif gender == 'f':
		females.append(age)

with open('Student_Data_19Sp.txt', 'w') as file:
	# Write header
	file.write('{: <10}'.format('Gender'))
	file.write('{: <22}'.format('Number of Students'))
	file.write('{: <14}'.format('Minimum Age'))
	file.write('{: <14}'.format('Maximum Age'))
	file.write('\n')

	# Write female row
	file.write('{: <10}'.format('Female'))
	file.write('{: <22}'.format(len(females)))
	file.write('{: <14}'.format(min(females)))
	file.write('{: <14}'.format(max(females)))
	file.write('\n')

	# Write male row
	file.write('{: <10}'.format('Male'))
	file.write('{: <22}'.format(len(males)))
	file.write('{: <14}'.format(min(males)))
	file.write('{: <14}'.format(max(males)))
	file.write('\n')
