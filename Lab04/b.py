# By submitting this assignment, we agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "We have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani, Grant Trusty, Collin Stafford, Braeden Stewart
# Section:     219
# Assignment:  04 Program 2
# Date:        15 September 2020

# Goal: Use a model developed by the NIH to estimate a person’s 10-year risk for likelihood of a heart attack. To make this slightly less time-consuming, only handle Women from 20 to 59 years of age.

DEBUG = False

print('Goal: \nUse a model developed by the NIH to estimate a person’s 10-year risk for likelihood of a heart attack. To make this slightly less time-consuming, only handle Women from 20 to 59 years of age.')
print()

print('This model works for women between the ages of 20 and 59.')

# ============ USER INPUT =============
age            = int(input('What is your age, as a number?\n\t> '))
cholesterol    = int(input('What is your cholesterol level?\n\t> '))
smoker         =     input('Do you smoke [Y/n]?\n\t> ').lower().startswith('y')
HDL            = int(input('What is your HDL, in mg/dL?\n\t> '))
blood_pressure = int(input('What is your systolic blood pressure, in mmHg?\n\t> '))
treated        =     input('Do you take medication for your BP [Y/n]?\n\t> ').lower().startswith('y')

# ============ CALCULATIONS ===========
points = 0

# ---------- age ----------
# age_range is used to compute point values for later attributes
if age < 35:
    points += -7
    age_range = 0
elif age < 40:
    points += -3
    age_range = 0
elif age < 45:
    points += 0
    age_range = 1
elif age < 50:
    points += 3
    age_range = 1
elif age < 55:
    points += 6
    age_range = 2
else:
    points += 8
    age_range = 2

if DEBUG: print(f'{points} points after age')

# ---------- cholesterol ----------
if cholesterol < 160:
    pass          # points += 0
elif cholesterol < 200:
    points += [4, 3, 2][age_range]
elif cholesterol < 240:
    points += [8, 6, 4][age_range]
elif cholesterol < 280:
    points += [11, 8, 5][age_range]
else:
    points += [13, 10, 7][age_range]

if DEBUG: print(f'{points} points after cholesterol')

# ---------- smoker ----------
if smoker:
    points += [9, 7, 4][age_range]

if DEBUG: print(f'{points} points after smoking')

# ---------- HDL ----------
if HDL < 40:
    points += 2
elif HDL < 50:
    points += 1
elif HDL < 60:
    pass         # points += 0
else:
    points += -1

if DEBUG: print(f'{points} points after HDL')

# ---------- blood pressure ----------
if blood_pressure < 120:
    pass         # points += 0
elif blood_pressure < 130:
    points += [1, 3][treated]
elif blood_pressure < 140:
    points += [2, 4][treated]
elif blood_pressure < 160:
    points += [3, 5][treated]
else: 
    points += [4, 6][treated]

if DEBUG: print(f'{points} points after blood pressure')

# ======== CONVERSION TO RISK =========

if   points < 9:  risk = '<1'
elif points < 13: risk = '1'
elif points < 14: risk = '2'
elif points < 16: risk = '3'
elif points < 17: risk = '4'
elif points < 18: risk = '5'
elif points < 19: risk = '6'
elif points < 20: risk = '8'
elif points < 21: risk = '11'
elif points < 22: risk = '14'
elif points < 23: risk = '17'
elif points < 24: risk = '22'
elif points < 25: risk = '27'
else: risk = '≥30'

print(f'Given this information, you are at a {risk}% 10-year risk for a heart attack.')
