import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, K = map(int, input().split())
	A = list(map(int, input().split()))

	ans = 0
	# 숫자: 숫자의 숫자
	d = dict()
	e = 0
	for s in range(N):
		while e < N and (A[e] not in d or d[A[e]] < K):
			if A[e] not in d:
				d[A[e]] = 0
			d[A[e]] += 1
			e += 1
		
		ans = max(ans, e-s)
		d[A[s]] -= 1
	print(ans)

main()