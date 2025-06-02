import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = float('inf')

def main():
    for _ in range(int(input())):
        N, M, K = map(int, input().split())
        graph = [[] for _ in range(N+1)]
        for _ in range(K):
            u, v, c, d = map(int, input().split())
            graph[u].append((v, c, d))
        
        dp = [[MAX] * (M+1) for _ in range(N+1)]
        dp[1][0] = 0

        for cost in range(M+1):
            for node in range(N+1):
                if dp[node][cost] < MAX:
                    for nextNode, nextCost, nextTime in graph[node]:
                        if cost + nextCost <= M and dp[node][cost] + nextTime < dp[nextNode][cost + nextCost]:
                            dp[nextNode][cost + nextCost] = dp[node][cost] + nextTime

        result = min(dp[N])
        print(result if result != MAX else "Poor KCM")

main()