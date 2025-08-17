import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	move = ((1, 0), (-1, 0), (0, 1), (0, -1))
	for _ in range(int(input())):
		H, W, O, F, Xs, Ys, Xe, Ye = map(int, input().split())
		board = [[0] * W for _ in range(H)]

		for _ in range(O):
			x, y, l = map(int, input().split())
			board[x-1][y-1] = l
		
		visited = [[-1] * W for _ in range(H)]
		q = deque([(Xs-1, Ys-1, F)])
		visited[Xs-1][Ys-1] = F
		while q:
			x, y, f = q.popleft()
			if x == Xe-1 and y == Ye-1:
				print("잘했어!!")
				break
			for mx, my in move:
				nx, ny = x + mx, y + my
				if not (0 <= nx < H and 0 <= ny < W) or f <= 0:
					continue
				if f < board[nx][ny] - board[x][y]:
					continue

				if f - 1 > visited[nx][ny]:
					visited[nx][ny] = f - 1
					q.append((nx, ny, f - 1))
		else:
			print("인성 문제있어??")

main()