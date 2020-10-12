# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  07b Program 1
# Date:        06 10 2020

lst = [[1, 2], [2, 5], [3, 2]]

# max_sum = max(lst, key=sum)?
m = lst[0]
for l in lst:
	if sum(l) > sum(m):
		m = l

print(f'The sum of the list {m} is {sum(m)}, which is the highest in the list.')
