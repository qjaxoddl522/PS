import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, M, K = map(int, input().split())
	board = [input() for _ in range(N)]

	prefixW = [[0] * (M+1) for _ in range(N+1)]
	prefixB = [[0] * (M+1) for _ in range(N+1)]
	for i in range(N):
		for j in range(M):
			if (i + j) % 2 == 0:
				prefixW[i+1][j+1] = prefixW[i+1][j] + prefixW[i][j+1] +\
					  (1 if board[i][j] != 'W' else 0) - prefixW[i][j]
				prefixB[i+1][j+1] = prefixB[i+1][j] + prefixB[i][j+1] +\
					  (1 if board[i][j] != 'B' else 0) - prefixB[i][j]
			else:
				prefixW[i+1][j+1] = prefixW[i+1][j] + prefixW[i][j+1] +\
					  (1 if board[i][j] != 'B' else 0) - prefixW[i][j]
				prefixB[i+1][j+1] = prefixB[i+1][j] + prefixB[i][j+1] +\
					  (1 if board[i][j] != 'W' else 0) - prefixB[i][j]
	
	ans = K * K
	for i in range(N-K+1):
		for j in range(M-K+1):
			ans = min(ans, prefixW[i+K][j+K] - prefixW[i+K][j] - prefixW[i][j+K] + prefixW[i][j])
			ans = min(ans, prefixB[i+K][j+K] - prefixB[i+K][j] - prefixB[i][j+K] + prefixB[i][j])
	print(ans)

main()