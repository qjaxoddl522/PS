import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
from bisect import bisect_left, bisect_right

def main():
	"""
	인덱스를 담은 채로 x좌표 순서대로 정렬 (도착지를 구분하기 위함)
	인덱스를 x좌표 순서로, 구간에 최소 y값을 담은 세그먼트 트리 생성하고 방문했을 경우 INF로 업데이트
	이분 탐색으로 이동 가능한 x범위를 검색하여 최소 y값이 이동 가능한 블럭이 있을 경우 방문처리 및 트리 갱신
	탐색 중 N-1번 노드를 발견하면 이동 가능하므로 탐색 종료
	"""
	INF = float('inf')

	def update(idx, value):
		i = leafL + idx
		tree[i] = value
		while i > 1:
			i //= 2
			if tree[i*2][0] < tree[i*2+1][0]:
				tree[i] = tree[i*2]
			else:
				tree[i] = tree[i*2+1]

	def query(start, end):
		def find(idx, s, e):
			if s > end or e < start:
				return (INF, -1, -1)
			if start <= s and e <= end:
				return tree[idx]
			mid = (s + e) // 2
			left = find(idx*2, s, mid)
			right = find(idx*2+1, mid+1, e)
			if left[0] < right[0]:
				return left
			return right
		return find(1, 0, leafL-1)

	for _ in range(int(input())):
		N, a, b = map(int, input().split())
		blocks = [list(map(int, input().split())) for _ in range(N)]
		# (x값, y값, 정렬 전 블럭 인덱스)
		blocks = sorted([(x, y, i) for i, (x, y) in enumerate(blocks)])
		
		leafL = 1 << (N - 1).bit_length()
		# (y값, 블럭 인덱스, 트리 인덱스)
		tree = [(INF, -1, -1)] * (leafL * 2)
		for i in range(N):
			tree[leafL + i] = (blocks[i][1], blocks[i][2], i)
		for i in range(leafL-1, 0, -1):
			if tree[i*2][0] <= tree[i*2+1][0]:
				tree[i] = tree[i*2]
			else:
				tree[i] = tree[i*2+1]
		
		q = deque()
		for i in range(N):
			if blocks[i][1] <= b:
				q.append(i)
				update(i, (INF, -1, -1))
		while q:
			idx = q.popleft()
			block = blocks[idx]
			if blocks[idx][2] == N-1:
				print("YES")
				break
			
			start = bisect_left(blocks, (block[0] - a, -INF))
			end = bisect_right(blocks, (block[0] + a, INF)) - 1
			while True:
				minY, _, nextIdx = query(start, end)
				if block[1] + b >= minY:
					q.append(nextIdx)
					update(nextIdx, (INF, -1, -1))
				else:
					break
		else:
			print("NO")

main()