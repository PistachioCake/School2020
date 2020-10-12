# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  07b Program 3
# Date:        06 10 2020

sentence = input('Enter a sentence (without punctuation) to convert into Pig Latin.\n\t> ')
words = sentence.split()

words = [word + 'yay' if word[0].lower() in 'aeiou' else word[1:] + word[0] + 'ay' for word in words]

print(' '.join(words))
