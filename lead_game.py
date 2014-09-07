# Lead Game
import sys
	

n = int(input())
a = sys.stdin.readlines()
max_a = 0
max_b = 0
lead_a = 0 
lead_b = 0
max_lead = 0
for each_record in a:
	(score_a,score_b) = map(int,each_record.split())
	lead_a += score_a
	lead_b += score_b
	diff=lead_a-lead_b
	if (abs(max_lead)<abs(diff)):
		max_lead = diff
	

if (max_lead>0):
	print ("1 "+str(max_lead))
else :
	print ("2 "+str(max_lead))
	
			
				
