import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	"""
	두 쿼리를 나눠서 개별로 저장
	2번 쿼리들을 k 순서대로 정렬하고 1번 쿼리를 수행할 때마다 2번 쿼리에 있는 k번을 수행하며 원래 순서와 결과를 저장
	수행이 끝나면 원래 순서대로 재정렬 후 결과 출력
	"""
	N = int(input())
	A = list(map(int, input().split()))
	M = int(input())

	q1 = []; q2 = []
	for i in range(M):
		inp = list(map(int, input().split()))
		if inp[0] == 1:
			q1.append(inp[1:])
		elif inp[0] == 2:
			q2.append(inp[1:] + [i])
	q2.sort(key= lambda x: x[0])
	
	def update(idx, value):
		idx += leafL
		tree[idx] = value
		idx //= 2
		while idx > 0:
			tree[idx] = tree[idx*2] + tree[idx*2+1]
			idx //= 2

	def query(l, r):
		l += leafL; r += leafL
		sum = 0
		while l <= r:
			if l & 1:
				sum += tree[l]
				l += 1
			if not r & 1:
				sum += tree[r]
				r -= 1
			l //= 2; r //= 2
		return sum

	# 트리 생성
	leafL = 1 << (N-1).bit_length()
	tree = [0] * (leafL * 2)
	for i in range(N):
		tree[leafL+i] = A[i]
	for i in range(leafL-1, 0, -1):
		tree[i] = tree[i*2] + tree[i*2+1]
	
	# 쿼리 수행
	ans = []
	q2Idx = 0
	for i in range(len(q1)+1):
		while q2Idx < len(q2) and q2[q2Idx][0] == i:
			res = query(q2[q2Idx][1]-1, q2[q2Idx][2]-1)
			ans.append((q2[q2Idx][3], res))
			q2Idx += 1
		if i < len(q1):
			update(q1[i][0]-1, q1[i][1])
	
	# 원래 순서대로 정렬 후 출력
	ans.sort()
	for i in range(len(ans)):
		print(ans[i][1])

main()