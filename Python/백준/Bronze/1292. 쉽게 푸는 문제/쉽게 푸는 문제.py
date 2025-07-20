import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	A, B = map(int, input().split())
	N = 1
	repeat = 0
	ans = 0
	for i in range(1, B+1):
		if repeat < N:
			repeat += 1
		else:
			N += 1
			repeat = 1
		if A <= i:
			ans += N
	print(ans)

main()