import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(1_000_000)

def main():
	N = int(input())
	edges = [tuple(map(int, input().split())) for _ in range(N-1)]
	weights = [0] + [int(input()) for _ in range(N)]
	g = [[] for _ in range(N+1)]
	for u, v in edges:
		g[u].append(v)
		g[v].append(u)

	S = sum(weights[1:])
	visited = [False] * (N+1)
	parent = [0] * (N+1)
	sub = [0] * (N+1)

	def dfs(u):
		visited[u] = True
		s = weights[u]
		for v in g[u]:
			if not visited[v]:
				parent[v] = u
				s += dfs(v)
		sub[u] = s
		return s

	dfs(1)

	best = float('inf')
	cutEdge = None
	for u in range(2, N+1):
		diff = abs(S - sub[u] * 2)
		if diff < best:
			best = diff
			cutEdge = (u, parent[u])

	print(best)
	print(*cutEdge)

main()