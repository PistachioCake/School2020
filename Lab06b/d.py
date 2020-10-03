# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  06b Program 4
# Date:        30 09 2020

# ----------------- Populate the creds ----------

n = int(input('How many credentials are there? '))

credentials = {}

for _ in range(n):
	username = input('Username: ')
	password = input('Password: ')
	credentials[username] = password
	print()

print('-' * 50)

# ----------------- Log in a user ---------------

print('Logging in.')

# Loop until break
while True:
	print()
	username = input('Username: ')
	password = input('Password: ')
	# check if the username exists and the password is associated with it
	if username in credentials and credentials[username] == password:
		print('Welcome!')
		break
	print('Try again.')



