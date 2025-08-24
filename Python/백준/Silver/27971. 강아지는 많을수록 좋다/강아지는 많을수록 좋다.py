import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, M, A, B = map(int, input().split())
	possible = set(range(N+1))
	for _ in range(M):
		l, r = map(int, input().split())
		for i in range(l, r+1):
			possible.discard(i)

	dp = [float('inf')] * (N+1)
	dp[0] = 0
	for i in range(N):
		if dp[i] == float('inf'):
			continue
		if i + A <= N and i + A in possible:
			dp[i+A] = min(dp[i+A], dp[i] + 1)
		if i + B <= N and i + B in possible:
			dp[i+B] = min(dp[i+B], dp[i] + 1)
	print(dp[N] if dp[N] != float('inf') else -1)

main()