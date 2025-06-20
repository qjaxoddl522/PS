import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
	INF = float('inf')
	move = ((1, 0), (0, 1), (-1, 0), (0, -1))

	N = int(input())
	board = [list(map(int, input().split())) for _ in range(N)]

	soliders = []
	army = -1
	for i in range(N):
		for j in range(N):
			if board[i][j] == 0:
				soliders.append((i, j))
			elif board[i][j] == -1:
				army = (i, j)
				board[i][j] = 0
	
	def dijkstra(sr, sc):
		visit = [[False] * N for _ in range(N)]
		cost = [[INF] * N for _ in range(N)]
		cost[sr][sc] = 0
		hq = [(0, sr, sc)]
		while hq:
			co, r, c = heappop(hq)
			if visit[r][c]:
				continue
			visit[r][c] = True
			for mr, mc in move:
				nr, nc = r + mr, c + mc
				if not (0 <= nr < N and 0 <= nc < N):
					continue
				if visit[nr][nc]:
					continue
				
				if co + board[nr][nc] < cost[nr][nc]:
					cost[nr][nc] = co + board[nr][nc]
					heappush(hq, (cost[nr][nc], nr, nc))
		return cost
	
	cost = []
	armyToOthers = []
	for i in range(len(soliders)):
		c = dijkstra(*soliders[i])
		other = []
		for j in range(len(soliders)):
			other.append(c[soliders[j][0]][soliders[j][1]])
		armyToOthers.append(c[army[0]][army[1]])
		cost.append(other)
	armyToOthers.append(0)
	cost.append(armyToOthers)
	soliders.append(army)

	result = INF
	visit = [False] * (len(soliders) - 1)
	def bt(node, co, visited):
		nonlocal result
		if visited == len(soliders) - 1:
			result = min(result, co + cost[-1][node])
			return
		
		for i in range(len(soliders)-1):
			if node != i and not visit[i]:
				visit[i] = True
				bt(i, co + cost[node][i], visited + 1)
				visit[i] = False
	bt(len(soliders) - 1, 0, 0)
	print(result)

main()