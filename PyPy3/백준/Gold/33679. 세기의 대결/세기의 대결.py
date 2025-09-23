import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    def Lis(doubled, s):
        dp = [1] * N
        best = 0
        for i in range(N):
            ai = doubled[s + i]
            for j in range(i):
                if ai > doubled[s + j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > best:
                best = dp[i]
        return best
    
    
    def GetMaxScore(ls):
        doubled = ls * 2
        ans = 0
        for s in range(N):
            ans = max(ans, Lis(doubled, s))
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