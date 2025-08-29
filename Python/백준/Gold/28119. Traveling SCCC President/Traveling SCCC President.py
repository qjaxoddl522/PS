import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	"""
	지금까지 방문했던 곳을 시간 소모하지 않고 이동할 수 있다.
	=> 모든 장소를 이으면 모든 곳을 시간 소모 없이 방문할 수 있다.
	=> 회의 순서와는 아무 상관 없고 모든 건물을 잇는 최소 스패닝 트리를 만들면 된다.
	"""
	N, M, _ = map(int, input().split())
	lines = []
	for _ in range(M):
		u, v, w = map(int, input().split())
		lines.append((w, u, v))
	map(int, input().split())
	lines.sort()

	root = [i for i in range(N+1)]
	rank = [0] * (N+1)

	def union(a, b):
		ra = find(a)
		rb = find(b)
		if rank[ra] < rank[rb]:
			root[ra] = rb
		elif rank[ra] > rank[rb]:
			root[rb] = ra
		else:
			root[ra] = rb
			rank[rb] += 1

	def find(a):
		if root[a] != a:
			root[a] = find(root[a])
		return root[a]

	ans = 0
	for w, u, v in lines:
		if find(u) != find(v):
			union(u, v)
			ans += w
	print(ans)

main()