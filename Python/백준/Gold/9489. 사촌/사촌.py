import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	while True:
		n, k = map(int, input().split())
		if n == 0 and k == 0:
			break
		ls = list(map(int, input().split()))
		
		tree = dict()
		parent = dict()
		upline = deque(['Trash'])
		nowLine = [ls[0]]
		for i in range(1, n):
			if ls[i] != ls[i-1] + 1:
				upline.popleft()
				if not upline:
					upline = deque(nowLine)
					nowLine = []
			
			if upline[0] not in tree:
				tree[upline[0]] = []
			tree[upline[0]].append(ls[i])
			parent[ls[i]] = upline[0]
			
			nowLine.append(ls[i])
		
		cousin = 0
		grand = parent.get(parent.get(k, 0), 0)
		if grand == 0:
			print(0)
			continue
		for p in tree[grand]:
			if p == parent[k]:
				continue
			if p in tree:
				cousin += len(tree[p])
		print(cousin)

main()