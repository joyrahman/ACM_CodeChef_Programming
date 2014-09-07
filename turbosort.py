#Turbo Sort
import sys

t = int(input())
#d = map(int, sys.stdin.readlines())
array  = map(int,sys.stdin.readlines())

#d.sort()
#array = []
"""for i in range (0,t):
	token = input()
	array.append(token)
	
array.sort()
"""
array.sort()
for i in array:
	print (i)	