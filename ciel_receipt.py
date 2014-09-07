import math
import pdb


def find_count(p):
    count = 0
    i = 11
    while p>0:
        N = math.pow(2,i)
        if p>= N:
            #pdb.set_trace()
            divisor = int(p/N)
            old = p
            p = p % N
            count += divisor 
            #print "p:{},N:{},d:{},c:{},p*:{},i:{}".format(old,N,divisor,count,p,i)
        #print "i:{}".format(i)
        i = i-1
    return count




T = int(raw_input())
while(T):
    p = int(raw_input())
    count = find_count(p)
    print count

    T -= 1
