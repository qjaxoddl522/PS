import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, M, K = map(int, input().split())
    skillInfo = [list(map(int, input().split())) for _ in range(N)]
    
    # dp[i][j] = i번째 스킬까지 사용하여 누적 데미지가 j일 때 사용한 최소 마나
    dp = [[float('inf')] * (M+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N+1):
        mana, deal = skillInfo[i-1]
        for dmg in range(M+1):
            # 현재 스킬 사용 횟수
            for p in range(dmg // deal, -1, -1):
                dp[i][dmg] = min(dp[i][dmg], dp[i-1][dmg-deal*p] 
                                 + mana * p + K * (p * (p - 1) // 2))
    print(dp[N][M])

main()