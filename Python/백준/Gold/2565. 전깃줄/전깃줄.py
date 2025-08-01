import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	lines = []
	for _ in range(N):
		lines.append(list(map(int, input().split())))
	lines.sort()

	seq = [lines[i][1] for i in range(N)]
	dp = [1] * N
	for i in range(N):
		for j in range(i):
			if seq[i] > seq[j]:
				dp[i] = max(dp[i], dp[j] + 1)
	print(N-max(dp))
	
main()