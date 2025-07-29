import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	n = int(input())
	grape = [0] + [int(input()) for _ in range(n)]

	# dp[i번째 포도주][연속 개수]
	dp = [[0] * 3 for _ in range(n+1)]
	for i in range(1, n+1):
		dp[i][0] = max(dp[i-1])
		dp[i][1] = max(dp[i-2]) + grape[i]
		dp[i][2] = dp[i-1][1] + grape[i]
	print(max(dp[n]))

main()