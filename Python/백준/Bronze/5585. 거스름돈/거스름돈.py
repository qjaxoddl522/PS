import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = 1000 - int(input())
	money = [500, 100, 50, 10, 5, 1]
	ans = 0
	for m in money:
		ans += N // m
		N %= m
	print(ans)

main()