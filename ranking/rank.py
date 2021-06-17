'''
	rank.py

	Ranks a list of items from a text file by asking a series of comparisons.
	Basically a sorting algorithm but all comparisons are prompts

	Author: Kyle M
	Created 22 May 2021
'''

from random import *

# compares two items by a user prompt
#
# params:
# 	a = first thing to compare
# 	b = second thing to compare
# return:
# 	true if a is considered above b, false otherwise
import sys


def compare(a, b):
	print(a, '[1] or', b, '[2]?')
	i = 0
	while i != 1 and i != 2:
		i = int(input())
	return i == 1


# sorts a list using recursive quicksort, except the comparisons are given by user input
#
# params:
# 	arr = any list
# return:
# 	the sorted list
def quicksort(arr):

	# base case: arr has one or zero elements
	if len(arr) <= 1:
		return arr

	# get center index
	center = arr.pop(len(arr) // 2)

	# split the rest into smaller and larger than the center
	left = []
	right = []
	for x in arr:
		if compare(x, center):
			left.append(x)
		else:
			right.append(x)

	# recursion recursion recursion recursion recursion
	left = quicksort(left)
	right = quicksort(right)

	# construct da list
	left.append(center)
	left.extend(right)
	return left


# ============================================================================
# MAIN PROCESSING
# ============================================================================

# read from a text file and sort
if len(sys.argv) == 2:
        filename = sys.argv[1]
else:
        filename = input('text file of stuff to rank? ')

ranking = open(filename).readlines()
for i in range(0, len(ranking) - 1):
	ranking[i] = ranking[i][0:-1]
shuffle(ranking)
ranking = quicksort(ranking)

# print the results
print('\n\nTHE RANKING:')
for i in range(0, len(ranking)):
	print(str(i+1) + ') ' + ranking[i])
