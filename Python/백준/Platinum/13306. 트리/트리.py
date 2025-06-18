import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	"""
	N-1번의 간선을 끊는 쿼리를 모두 수행하면 아무것도 연결되어 있지 않음
	거꾸로 수행하며 0번 쿼리가 뜰 때마다 간선을 이어붙이면 1번 쿼리를 정상적으로 수행 가능
	결과는 거꾸로 출력하여 정상적으로 출력
	"""

	def union(a, b):
		ra = find(a); rb = find(b)
		if rank[ra] > rank[rb]:
			root[rb] = ra
		elif rank[ra] < rank[rb]:
			root[ra] = rb
		else:
			root[rb] = ra
			rank[ra] += 1
	
	def find(a):
		if root[a] != a:
			root[a] = find(root[a])
		return root[a]

	N, Q = map(int, input().split())
	rank = [0] * (N+1)
	root = [i for i in range(N+1)]
	parent = [0, 1]
	for _ in range(N-1):
		parent.append(int(input()))
	
	result = []
	query = [list(map(int, input().split())) for _ in range(N-1+Q)]
	for q in reversed(query):
		if q[0] == 0:
			union(q[1], parent[q[1]])
		elif q[0] == 1:
			if find(q[1]) == find(q[2]):
				result.append("YES")
			else:
				result.append("NO")
	print(*reversed(result), sep='\n')

main()