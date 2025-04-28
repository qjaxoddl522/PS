import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    L = list(map(int, input().split()))
    J = list(map(int, input().split()))

    dp = [0] * 100
    
    for i in range(N):
        for happy in range(99, 0, -1):
            if happy - L[i] >= 0:
                dp[happy] = max(dp[happy], dp[happy - L[i]] + J[i])
    print(dp[99])

main()