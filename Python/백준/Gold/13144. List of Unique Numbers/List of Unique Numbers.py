import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	ls = list(map(int, input().split()))
	visited = [False] * 100001
	
	ans = 0
	e = 0
	for s in range(N):
		while e < N:
			if visited[ls[e]]:
				break
			visited[ls[e]] = True
			e += 1
		ans += e - s
		visited[ls[s]] = False
	print(ans)

main()