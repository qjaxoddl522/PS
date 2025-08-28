import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, M = map(int, input().split())
	order = list(map(int, input().split()))
	cost = [tuple(map(int, input().split())) for _ in range(N-1)]

	# 간 각선들의 사용 횟수 구간합
	diff = [0] * N
	for i in range(1, M):
		a = order[i-1] - 1
		b = order[i] - 1
		if a > b:
			a, b = b, a
		diff[a] += 1
		diff[b] -= 1
	
	ans = 0
	used = 0
	for i in range(N-1):
		used += diff[i]
		ticket = cost[i][0] * used
		card = cost[i][2] + cost[i][1] * used
		ans += min(ticket, card)
	print(ans)

main()