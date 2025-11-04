import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    H = list(map(int, input().split()))
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))

    # 이분탐색으로 상자가 파손되지 않는 최대 j(i > j)를 구하기
    def FindMaxIdx(i):
        l, r = 0, i-1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if H[mid] >= H[i] + B[i]:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        return res

    # dp[계단 인덱스] = 최대 점수
    dp = [0] * (N)
    for i in range(N):
        j = FindMaxIdx(i)
        dp[i] = max(dp[i-1], dp[j] + A[i] if j >= 0 else 0)
    
    print(dp[N-1])
    
main()