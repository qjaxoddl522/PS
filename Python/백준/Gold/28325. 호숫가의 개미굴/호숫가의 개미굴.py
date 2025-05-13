import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    C = list(map(int, input().split()))
    
    # 첫번째 방 사용 여부에 따라 다르게
    def dynamic(isStartUse):
        # 0: 방 사용, 1: 쪽방 사용
        dp0, dp1 = (1, -1) if isStartUse else (-1, C[0])
        for i in range(1, N):
            ndp0 = dp1 + 1
            ndp1 = max(dp0, dp1) + C[i]

            if i == N - 1 and isStartUse:
                ndp0 = -1
            dp0, dp1 = ndp0, ndp1
        return max(dp0, dp1)
        
    print(max(dynamic(False), dynamic(True)))

main()