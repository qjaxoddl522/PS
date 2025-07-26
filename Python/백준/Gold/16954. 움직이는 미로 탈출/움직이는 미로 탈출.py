import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	N = 8
	board = [list(input()) for _ in range(N)]
	visited = [[[False] * N for _ in range(N)] for _ in range(N)]
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
	              (-1, -1), (-1, 1), (1, -1), (1, 1), 
	              (0, 0)]
	
	# r, c, 시간(이동한 벽의 거리)
	q = deque([(7, 0, 0)])
	while q:
		r, c, t = q.popleft()
		for dr, dc in directions:
			nr, nc = r + dr, c + dc
			if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc][t+1]:
				continue
			# 이동하는 벽까지 고려하여 갈 수 있는지 확인
			if (nr-t >= 0 and board[nr-t][nc] == '#') or (nr-t >= 1 and board[nr-t-1][nc] == '#'):
				continue
			if t == N - 2:
				print(1)
				return
			visited[nr][nc][t+1] = True
			q.append((nr, nc, t + 1))
	print(0)

main()