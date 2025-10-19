import sys
input = lambda: sys.stdin.readline().rstrip()

def Main():
    N = int(input())
    M = int(input())

    isVip = bytearray(N+1)
    for _ in range(M):
        isVip[int(input())] = True

    # dp[좌석번호] = 좌석에 앉을 수 있는 경우의 수
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        # 정상적으로 앉기
        dp[i] += dp[i-1]
        # vip 자리가 아니면 바꿔앉기
        if i > 1 and not isVip[i] and not isVip[i-1]:
            dp[i] += dp[i-2]
    print(dp[N])

Main()