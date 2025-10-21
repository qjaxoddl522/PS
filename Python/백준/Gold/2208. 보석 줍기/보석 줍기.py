import sys
input = lambda: sys.stdin.readline().rstrip()

def Main():
    N, M = map(int, input().split())
    values = [int(input()) for _ in range(N)]
    ans = 0
    prefix = [0] * (N+1)
    for i in range(N):
        prefix[i+1] = prefix[i] + values[i]
    
    # 인덱스 차이가 M 이상인 누적합 최대 - 최소 구하기
    minPrefix = prefix[0]
    for r in range(M, N+1):
        minPrefix = min(minPrefix, prefix[r-M])
        ans = max(ans, prefix[r] - minPrefix)
    print(ans)

Main()