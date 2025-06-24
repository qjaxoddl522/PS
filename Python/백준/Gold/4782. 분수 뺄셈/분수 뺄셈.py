import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	def gcd(a, b):
		if b <= 0:
			return a
		return gcd(b, a % b)

	while True:
		b, n = map(int, input().split())
		if b == 0 and n == 0:
			break

		g = gcd(b, n)
		nn = n // g
		for m in range(n * 2, nn - 1, -nn):
			fa = (b * m * (2 * n - m)) / n ** 2
			a = int(fa)
			if a != fa:
				continue
			if a != b and m != n:
				print(f"{a}/{m}", end=' ')
		print()

main()