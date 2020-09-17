# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  04b Program 2
# Date:        DD MM YYYY

while True:
	units = input('Which units would you like to use? [M]etric or [I]mperial?\n\t> ').lower()
	if units in ['m', 'metric']:
		metric = True
		break
	elif units in ['i', 'imperial']:
		metric = False
		break
	else:
		print('Please enter M for metric units (cm, kg) or I for imperial units (lb, in).')

weight = float(input(f"What is your weight? ({'kg' if metric else 'in'})\n\t> "))
print(weight)
height = float(input(f"What is your height? ({'cm' if metric else 'lb'})\n\t> "))
print(height)

bmi = weight / height ** 2 * (10000 if metric else 703)

status = 'underweight' if bmi < 18.5 else \
         'healthy'     if bmi < 25   else \
         'overweight'  if bmi < 30   else \
         'obese'

print(f'Your body mass index is {bmi:.3f}, which is considered {status}.')
