import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    def Lis(seq):
        tails = []
        for x in seq:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
    
    def GetMaxScore(ls):
        doubled = ls * 2
        ans = 0
        for s in range(N):
            ans = max(ans, Lis(doubled[s:s+N]))
        return ans
    
    yj = GetMaxScore(A)
    hg = GetMaxScore(B)
    
    if yj > hg:
        print("YJ Win!")
    elif yj < hg:
        print("HG Win!")
    else:
        print("Both Win!")

main()