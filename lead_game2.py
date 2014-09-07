import sys
 
def main():
    nRounds = int(sys.stdin.readline())
    max_lead = 0
    score_p1 = 0
    score_p2 = 0
    for d in sys.stdin.readlines():
        round_p1, round_p2 = map(int, d.split())
        score_p1 += round_p1
        score_p2 += round_p2
        diff = score_p1 - score_p2
        print (diff)
        if abs(max_lead) < abs(diff):
            max_lead = diff
            print max_lead
    if max_lead > 0:
        print("1 {}".format(max_lead))
    else:
        print("2 {}".format(-max_lead))
 
if __name__ == '__main__':
    main()
