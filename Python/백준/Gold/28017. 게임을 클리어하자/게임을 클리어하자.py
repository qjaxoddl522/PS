import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    time = []
    for _ in range(N):
        time.append(list(map(int, input().split())))
    
    # i번째 회차에서 j번째 무기를 선택했을 때 최소 시간
    dp = [[float('inf')] * M for _ in range(N)]
    for j in range(M):
        dp[0][j] = time[0][j]
    for i in range(1, N):
        # 앞에서부터 최소, 뒤에서부터 최소 누적
        firstMin = dp[i][0]
        lastMin = dp[i][M-1]

        for j in range(M):
            dp[i][j] = min(dp[i][j], firstMin)
            firstMin = min(firstMin, dp[i-1][j])
        
            dp[i][M-j-1] = min(dp[i][M-j-1], lastMin)
            lastMin = min(lastMin, dp[i-1][M-j-1])

        for j in range(M):
            dp[i][j] += time[i][j]
    
    print(min(dp[N-1]))

main()