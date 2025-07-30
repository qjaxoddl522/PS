import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	lines = [tuple(map(int, input().split())) for _ in range(N)]
	lines.sort()

	ans = 0
	seq = [-1000000000, -1000000000]
	for s, e in lines:
		if seq[1] < s:
			seq = [s, e]
			ans += e - s
		else:
			ans += max(0, e - seq[1])
			seq[1] = max(seq[1], e)
	print(ans)

main()