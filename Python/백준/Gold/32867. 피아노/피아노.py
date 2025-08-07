import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, K = map(int, input().split())
	A = list(map(int, input().split()))

	ans = 0
	left, right = 0, 0
	for a in A:
		left = min(left, a) if left != 0 else a
		right = max(right, a)

		if right - left >= K:
			left = a
			right = a
			ans += 1
	print(ans)

main()