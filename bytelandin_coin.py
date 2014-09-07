import math
mem = {0:0}

def find_max_profit(n):
    n1 = n/2
    n2 = n/3
    n3 = n/4

    if n in mem:
        return mem[n]
    else:
        n1 = max(n1, find_max_profit(n1))
        n2 = max(n2, find_max_profit(n2))
        n3 = max(n3, find_max_profit(n3))

        mem[n] = max(n,n1+n2+n3)
        return mem[n]

while True:
    try:
        x = raw_input()
        print find_max_profit(int(x))
        print mem
    except:
        break
