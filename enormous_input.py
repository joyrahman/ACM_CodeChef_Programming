#enormous input test
import sys

read_line = raw_input().split()
no_of_lines = int(read_line[0])
divisor = int(read_line[1])
count = 0
t = map(int,sys.stdin.readlines())

for i in t:
        #t = int(input())
        if (i%divisor==0):
                count = count + 1
print (count)    
