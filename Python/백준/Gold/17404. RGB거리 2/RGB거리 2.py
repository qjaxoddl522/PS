import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	cost = [list(map(int, input().split())) for _ in range(N)]
	
	def dynamic(end):
		# i번째 집에서 j색을 골랐을 때 최소 비용
		dp = [[float('inf') for _ in range(3)] for _ in range(N-1)]
		for j in range(3):
			if j != end:
				dp[0][j] = cost[0][j]
		for i in range(1, N-1):
			dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
			dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
			dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
		if end == 0:
			return min(dp[N-2][1], dp[N-2][2]) + cost[N-1][0]
		if end == 1:
			return min(dp[N-2][0], dp[N-2][2]) + cost[N-1][1]
		if end == 2:
			return min(dp[N-2][0], dp[N-2][1]) + cost[N-1][2]
	
	print(min(dynamic(i) for i in range(3)))

main()