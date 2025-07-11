import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	N, M = map(int, input().split())
	graph = [[] for _ in range(N+1)]
	for _ in range(M):
		A, B = map(int, input().split())
		graph[A].append(B)
		graph[B].append(A)
	
	# 시작점과 친구면 True
	friend = [None] * (N+1)
	for start in range(1, N+1):
		if friend[start] != None:
			continue

		friend[start] = True
		q = deque([start])
		while q:
			p = q.popleft()
			for np in graph[p]:
				if friend[np] == None:
					friend[np] = not friend[p]
					q.append(np)
				elif friend[np] == friend[p]:
					print(0)
					return
	print(1)

main()