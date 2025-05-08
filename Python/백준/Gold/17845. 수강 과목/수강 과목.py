import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    study = [list(map(int, input().split())) for _ in range(K)]

    # i까지 공부시간을 사용했을 때 최대 중요도
    dp = [0] * (N+1)
    for imp, cost in study:
        for time in range(N, cost-1, -1):
            dp[time] = max(dp[time], dp[time - cost] + imp)
    print(dp[N])

main()