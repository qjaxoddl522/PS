import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	n, k = map(int, input().split())
	tree = [[] for _ in range(n)]
	for _ in range(n-1):
		p, c = map(int, input().split())
		tree[p].append(c)
		tree[c].append(p)
	fruit = list(map(int, input().split()))

	# visited[노드 방문(과일 획득) 비트]
	visited = [False] * (1<<n)
	# 해당 비트에서 얻는 과일들 수
	apple = [0] * (1<<n)
	pear = [0] * (1<<n)

	ans = 0
	visited[1] = True
	apple[1] = int(fruit[0] == 1)
	pear[1]  = int(fruit[0] == 2)
	q = deque([(1, tree[0])])
	while q:
		mask, adj = q.popleft()
		if apple[mask] > k:
			continue
		ans = max(ans, pear[mask])

		for nx in adj:
			nMask = mask | (1<<nx)
			if visited[nMask]:
				continue
			visited[nMask] = True

			apple[nMask] = apple[mask] + (fruit[nx] == 1)
			pear[nMask] = pear[mask] + (fruit[nx] == 2)

			newAdj = adj.copy()
			newAdj.remove(nx)
			for nxx in tree[nx]:
				if (nMask >> nxx) & 1 == 0:
					newAdj.append(nxx)
			q.append((nMask, newAdj))
	print(ans)

main()