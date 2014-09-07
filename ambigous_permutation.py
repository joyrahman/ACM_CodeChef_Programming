# Ambiguous Permutation
import sys
def ambiguous (a,length):
	b=[]
	ambiguous = 1
	for i in range (0,length):
		#print ("a[i]:"+str(a[i])+"=> i"+str(i))
		b.insert(a[i]+1,i) 
		if (a[i]!=b[i]):
			ambiguous = 0
		else:
			continue	
#	print a,b		
	return ambiguous	

n = int(input())
a = []
b = []
while (n!=0):
	a = map(int,sys.stdin.readline().split())
	if (ambiguous(a,n)):
		print "ambiguous"
	else :
		print "non ambiguous"	
	
	n = int(input())

	





	
