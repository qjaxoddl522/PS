import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, M = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(N)]
	prefix = [[0] * (M+1) for _ in range(N+1)]
	
	for i in range(1, N+1):
		prefixHor = 0
		for j in range(1, M+1):
			prefixHor += board[i-1][j-1]
			prefix[i][j] = prefix[i-1][j] + prefixHor
	
	K = int(input())
	for _ in range(K):
		i, j, x, y = map(int, input().split())
		print(prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1])

main()