import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	C, N = map(int, input().split())
	ef = [tuple(map(int, input().split())) for _ in range(N)]
	dp = [float('inf') for _ in range(C+100)]

	dp[0] = 0
	for cost, people in ef:
		for i in range(people, C+100):
			dp[i] = min(dp[i], dp[i-people] + cost)
	print(min(dp[C:]))

main()