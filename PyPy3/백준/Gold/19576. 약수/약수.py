import sys
input = lambda: sys.stdin.readline().rstrip()

def Main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    
    # dp[A[i]를 포함하는 i번째 원소까지의 부분집합] = 모든 원소들이 약수-배수 관계인 최대 크기
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if A[i] % A[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    # N - (가장 많은 약수 - 배수 관계인 부분집합) = 바꿔야 하는 최소 숫자
    print(N - max(dp))

Main()