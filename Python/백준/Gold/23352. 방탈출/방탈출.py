import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	N, M = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(N)]

	maxDist = 0
	ans = 0

	# 시작점에서 최장거리 및 합 갱신
	def bfs(sr, sc):
		nonlocal maxDist, ans
		visited = [[False] * M for _ in range(N)]
		visited[sr][sc] = True
		q = deque([(sr, sc, 0)])
		while q:
			r, c, d = q.popleft()
			if d == maxDist:
				ans = max(ans, board[sr][sc] + board[r][c])
			elif d > maxDist:
				maxDist = d
				ans = board[sr][sc] + board[r][c]

			for mr, mc in move:
				nr, nc = r + mr, c + mc
				if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and board[nr][nc] != 0:
					q.append((nr, nc, d+1))
					visited[nr][nc] = True

	for i in range(N):
		for j in range(M):
			if board[i][j] != 0:
				bfs(i, j)
	print(ans)

main()