import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	N, K = map(int, input().split())
	# (현재 위치, 목표 위치)
	info = deque()
	for _ in range(K):
		X, R, C = map(int, input().split())
		r, c = (X - 1) // N, (X - 1) % N
		info.append([r, c, R-1, C-1])
	
	while info:
		r, c, ar, ac = info.popleft()
		# r행을 ac - c만큼 이동
		mc = (ac - c) % N
		# ac열을 ar - r만큼 이동
		mr = (ar - r) % N
		for i in range(len(info)):
			if info[i][0] == r:
				info[i][1] = (info[i][1] + mc) % N
			if info[i][1] == ac:
				info[i][0] = (info[i][0] + mr) % N
		print(abs(mr) + abs(mc))

main()