import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
	N = int(input())
	dist = [[1000] * N for _ in range(N)]
	for i in range(N):
		dist[i][i] = 0
	for _ in range(int(input())):
		a, b = map(int, input().split())
		dist[a-1][b-1] = 1
	
	for m in range(N):
		for s in range(N):
			for e in range(N):
				if dist[s][e] > dist[s][m] + dist[m][e]:
					dist[s][e] = dist[s][m] + dist[m][e]
	
	for i in range(N):
		missed = 0
		for j in range(N):
			if dist[i][j] == 1000 and dist[j][i] == 1000:
				missed += 1
		print(missed)

main()