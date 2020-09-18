# By submitting this assignment, We agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "We have not given or received any unauthorized aid on this assignment"
#
# Names: Rushil Udani, Collin Stafford, Braeden Stewart, Grant Trusty
# Section: 219
# Date: 19 September 2020

from math import sqrt, fabs

#---------------------------PART 1------------------------------#

# a = 1/7
# print(a)
# b = a * 7
# print(b)
# print("It printed 1 correctly.")
#
# c = 2*a
# d = 5*a
# e = c+d
# print(e)
# print("It did not round up to 1 correctly.")
#
# x = sqrt(1/3)
# print("x =", x)
# y = x*x*3
# print("x*x*3 =", y)
# print("Printed correctly.")
# z = x*3*x
# print("x*3*x =", z)
# print("Printed incorrectly.")



#---------------------------------------PART 2-----------------------------------------------#

#Define Constants
FIRST_STOP = 0.3
SECOND_GO = 0.4
INCREMENT = 0.1

#Obtain input from the user
current_increment = int(input("What increment is the rocket in? "))

#Calculate the distance the rocket has traveled
distance_traveled = current_increment * INCREMENT

#THIS IS THE PORTION OF PART 2 THAT DOESNT WORK DUE TO FLOATING POINT ERROR
# if distance_traveled == FIRST_STOP:
#	 print("Stop the first stage!")
# elif distance_traveled == SECOND_GO:
#	 print("Start the second stage!")
# else:
#	 print("No action required at this point.")


#------------------------------------------PART 3---------------------------------------------#

#Define tolerance (this is the smallest degree TOL can be where the program still works)

TOL = 1e-16

#Determines what output the user will receive

if (fabs(distance_traveled - FIRST_STOP)) < TOL:
	print("Stop the first stage!")
elif (fabs(distance_traveled - SECOND_GO)) < TOL:
	print("Start the second stage!")
else:
	print("No action required at this point.")
