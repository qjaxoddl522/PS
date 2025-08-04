import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	dist = list(map(int, input().split()))
	price = list(map(int, input().split()))

	ans = 0
	minPrice = 1000000000
	distSum = 0
	for i in range(N-1):
		if price[i] < minPrice:
			ans += distSum * minPrice
			distSum = 0
			minPrice = price[i]
		distSum += dist[i]
	ans += distSum * minPrice
	print(ans)

main()