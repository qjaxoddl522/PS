import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        lsN = list(map(int, list(input())))
        L = len(lsN)
        for i in range(L-1):
            if lsN[i] > lsN[i+1]:
                print(-1)
                break
        else:
            # 오른쪽부터 i번째 자릿수가 j일 때 증가하는 수의 개수
            dp = [[0] * 10 for _ in range(L+1)]
            for j in range(10):
                dp[1][j] = 1
            
            # 이전 자릿수보다 같거나 큰 숫자만 선택
            for i in range(2, L+1):
                for j in range(10):
                    for k in range(j, 10):
                        dp[i][j] += dp[i-1][k]
            
            ans = sum(dp[L])
            # N보다 큰 숫자 빼기
            for i in range(L):
                for j in range(lsN[i]+1, 10):
                    ans -= dp[L-i][j]
            # 자기 자신 제외
            print(ans-1)

main()