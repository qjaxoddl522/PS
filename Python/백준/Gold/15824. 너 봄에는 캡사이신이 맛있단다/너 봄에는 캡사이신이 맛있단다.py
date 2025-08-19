import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	MOD = 1000000007
	N = int(input())
	A = sorted(list(map(int, input().split())))
	
	ans = 0
	for i in range(N):
		ans = (ans + (pow(2, i, MOD) - 1) * (A[i] - A[N-i-1])) % MOD
	print(ans)

main()