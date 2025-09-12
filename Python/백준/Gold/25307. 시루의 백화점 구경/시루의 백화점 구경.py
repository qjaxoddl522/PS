import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	move = ((1, 0), (-1, 0), (0, 1), (0, -1))
	N, M, K = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(N)]

	visited = [bytearray(M) for _ in range(N)]
	q = deque()
	svisited = [bytearray(M) for _ in range(N)]
	sq = deque()

	for i in range(N):
		for j in range(M):
			if board[i][j] == 3:
				q.append((i, j))
				visited[i][j] = 1
				board[i][j] = 1
			elif board[i][j] == 4:
				sq.append((i, j))
				svisited[i][j] = 1
	
	# 거리 K까지만 확산
	for _ in range(K):
		if not q:
			break
		for _ in range(len(q)):
			r, c = q.popleft()

			for mr, mc in move:
				nr, nc = r + mr, c + mc
				if not (0 <= nr < N and 0 <= nc < M):
					continue
				if visited[nr][nc]:
					continue

				q.append((nr, nc))
				visited[nr][nc] = 1
				if board[nr][nc] != 4:
					board[nr][nc] = 1
	
	dist = 0
	while sq:
		for _ in range(len(sq)):
			r, c = sq.popleft()
			if board[r][c] == 2:
				print(dist)
				return

			for mr, mc in move:
				nr, nc = r + mr, c + mc
				if not (0 <= nr < N and 0 <= nc < M):
					continue
				if svisited[nr][nc] or board[nr][nc] == 1:
					continue
				
				sq.append((nr, nc))
				svisited[nr][nc] = 1
		dist += 1
	print(-1)

main()