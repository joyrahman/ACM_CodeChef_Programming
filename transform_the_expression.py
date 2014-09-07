# Reverse Polish Notification
import sys
 
def postfix(exp):
	stack=[]
	result=""
	for char in exp:
		if char==')':
			result+=stack.pop()
		elif char in '+-*/^':
			stack.append(char)
		elif char=='(':
			continue
		else:
			result+=char
	return result				
		
		
 
no_of_lines = int(input())
exps = sys.stdin.readlines()
#count =0
result=[]
for x in exps:	
	result.append(postfix(x))
    
for re in result:
	print re
