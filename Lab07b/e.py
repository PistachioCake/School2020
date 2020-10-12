# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  07b Program 5
# Date:        08 10 2020

scores = []
names = []

while True:
	score = int(input('Enter first score: '))
	if score < 0:
		break
	score += int(input('Enter second score: '))
	name = input('Enter name: ')
	scores.append(score)
	names.append(name)

print()
print()

# One algorithm to calculate the median
# This is O(n^2), which sucks, so I'm not doing it
# However, it would 
# 
# odd = len(scores) % 2 == 1
# median = []
# for score in scores:
# 	above = 0
# 	for s in scores:
# 		if score < s:
# 			above += 1
# 		elif score > s:
# 			above -= 1
# 	if odd:
# 		if above == 0:
# 			median.append(score)
# 	else:
# 		if above == 1 or above == -1:
# 			median.append(score)
# median = sum(median) / len(median)

def merge_sort(l, preserve=True):
	if len(l) < 2: return l
	if preserve: l = l[:]

	pivot = l.pop(0)

	# split l around pivot
	lower = []
	upper = []
	for e in l:
		if e > pivot: upper.append(e)
		else: lower.append(e)
	lower, upper = merge_sort(lower, False), merge_sort(upper, False)

	# merge lower and upper
	return lower + [pivot] + upper

def get_median(l):
	sorted_l = merge_sort(l)
	length = len(sorted_l)
	if length % 2:
		return sorted_l[length // 2]
	else:
		return (sorted_l[length // 2] + sorted_l[length // 2 - 1]) / 2

cut = get_median(scores)
passed = []
failed = []

for i in range(len(scores)):
	if scores[i] < cut:
		passed.append(names[i])
	else:
		failed.append(names[i])

print('Here are all the golfers that passed:')
print('\n'.join(passed))
print()
print('Here are all the golfers that failed:')
print('\n'.join(failed))


