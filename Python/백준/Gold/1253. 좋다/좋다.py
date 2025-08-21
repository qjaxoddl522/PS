import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	A = list(map(int, input().split()))

	ans = 0
	D = dict()
	for i in range(N):
		if A[i] not in D:
			D[A[i]] = 0
		D[A[i]] += 1
	
	for i in range(N-1):
		for j in range(i+1, N):
			s = A[i] + A[j]
			if s in D and \
			((A[i] != s and A[j] != s) or \
	 		(A[i] == A[j] and D[s] > 2) or \
			((A[i] != 0 or A[j] != 0) and (A[i] == s or A[j] == s) and D[s] > 1)):
				ans += D[s]
				del D[s]
	print(ans)

main()