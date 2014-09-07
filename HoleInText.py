#Hole in Text 
# A,D,O,P,Q,R 
# B
import sys
import re

no_of_lines = int(input())
t = sys.stdin.readlines()
#count =0 
for x in t:	
	count = 0
	count += 2*len(re.findall('B',x))
	count += len(re.findall(r"[ADOPQR]",x))
	print (count)	
   
    
#print (count)
