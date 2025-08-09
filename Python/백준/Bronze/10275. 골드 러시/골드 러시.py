import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	def index(n):
		return (n & -n).bit_length() - 1
	for _ in range(int(input())):
		n, a, b = map(int, input().split())
		print(n - index(a))

main()