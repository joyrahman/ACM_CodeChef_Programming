read_input = raw_input().split()
withdrawal = int(read_input[0])
init_balance = float(read_input[1])
charge  = .5
 
#success_flag = 0
#insufficient_flag = 0
#final_balance = 0
#if (withdrawal == 0):
#    success_flag = 1
#	print ('{:.2f}'.format(init_balance))
#    final_balance = init_balance
#    program_output(final_balance,success_flag,insufficient_flag)
    
if(withdrawal%5==0 and init_balance - withdrawal-charge >=0):
#   success_flag = 1
    print ('{:.2f}'.format(init_balance - withdrawal-charge))
else :    
	print ('{:.2f}'.format(init_balance))
		
#else :
#	print ("Incorrect Withdrawal Amount (not multiple of 5)")
#program_output(final_balance,success_flag,insufficient_flag)
