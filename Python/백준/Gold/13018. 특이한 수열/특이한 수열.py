import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, K = map(int, input().split())
	if K == N:
		print("Impossible")
		return
	
	ans = []
	for i in range(1, N-K):
		ans.append(i+1)
	ans.append(1)
	for i in range(N-K+1, N+1):
		ans.append(i)
	print(*ans)

main()