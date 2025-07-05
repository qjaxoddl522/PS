import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	move = ((1, 0), (0, 1), (-1, 0), (0, -1))
	board = [list(map(int, input().split())) for _ in range(5)]
	startR, startC = map(int, input().split())
	
	# 시작점으로부터의 위치와 이동 횟수를 반환
	def GetCost(str, stc, aim):
		if board[str][stc] == -1:
			return []

		visited = [[False] * 5 for _ in range(5)]
		visited[str][stc] = True
		# (r, c, 이동횟수)
		dq = deque([(str, stc, 0)])
		result = []
		while dq:
			r, c, moved = dq.popleft()
			if board[r][c] == aim:
				result.append((r, c, moved))
			
			for mr, mc in move:
				nr, nc = r + mr, c + mc
				if not 0 <= nr < 5 or not 0 <= nc < 5:
					continue
				if board[nr][nc] == -1 or visited[nr][nc]:
					continue
				visited[nr][nc] = True
				dq.append((nr, nc, moved + 1))

			for mr, mc in move:
				nr, nc = dash(r, c, mr, mc)
				if visited[nr][nc]:
					continue
				visited[nr][nc] = True
				dq.append((nr, nc, moved + 1))
		return result

	def dash(r, c, dr, dc):
		nr, nc = r, c
		while True:
			tr, tc = nr + dr, nc + dc
			if not (0 <= tr < 5 and 0 <= tc < 5):
				return nr, nc
			if board[tr][tc] == -1:
				return nr, nc
			nr, nc = tr, tc
			if board[nr][nc] == 7:
				return nr, nc

	ans = 999
	for r1, c1, cost1 in GetCost(startR, startC, 1):
		cost = cost1
		for r2, c2, cost2 in GetCost(r1, c1, 2):
			cost += cost2
			for r3, c3, cost3 in GetCost(r2, c2, 3):
				cost += cost3
				for r4, c4, cost4 in GetCost(r3, c3, 4):
					cost += cost4
					for r5, c5, cost5 in GetCost(r4, c4, 5):
						cost += cost5
						for _, _, cost6 in GetCost(r5, c5, 6):
							cost += cost6
							ans = min(ans, cost)
							cost -= cost6
						cost -= cost5
					cost -= cost4
				cost -= cost3
			cost -= cost2
	print(ans if ans < 999 else -1)

main()