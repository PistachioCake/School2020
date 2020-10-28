# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  10b Program 2
# Date:        28 10 2020

from csv import writer

# Get User input
amount = float(input('Amount of loan: '))
interest_rate_month = float(input('Interest Rate (%): ')) / 1200
payment_month = float(input('Monthly payment: '))
filename = input('Name for CSV File: ')

fileh = open(filename + '.csv', 'w', newline='')
filewriter = writer(fileh)

filewriter.writerow(['Month', 'Principal Balance', 'Accrued Interest'])

# If the loan will not be paid off, only write 30 months. Otherwise, write until the loan is 0.

if amount * interest_rate_month < payment_month:
	# added interest is below payment
	# i.e. this loan will be paid off
	month = 0
	total_interest = 0
	while amount >= 0:
		filewriter.writerow([month, amount, total_interest])
		interest_month = amount * interest_rate_month
		total_interest += interest_month
		month += 1
		amount += interest_month
		amount -= payment_month
else:
	# added interest is greater than payment
	# i.e. this loan will *not* be paid off
	for month in range(31):
		filewriter.writerowrow([month, amount, total_interest])
		interest_month = amount * interest_rate_month
		total_interest += interest_month
		amount += interest_month
		amount -= payment_month

fileh.close()
