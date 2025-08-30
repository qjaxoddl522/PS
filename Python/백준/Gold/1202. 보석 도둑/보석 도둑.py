import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
	"""
	보석을 무게 순서로 정렬하고, 낮은 무게의 가방부터 확인하면서 보석이 현재 가방보다 가벼울 경우 힙큐에 푸시.
	힙큐는 가치 내림차순으로 정렬하여 가방이 담을 수 있는 가장 높은 가치의 보석을 담는다.
	"""
	N, K = map(int, input().split())
	gem = [tuple(map(int, input().split())) for _ in range(N)]
	gem.sort()
	bag = sorted([int(input()) for _ in range(K)])

	gemIdx = 0
	hq = []
	ans = 0
	for b in bag:
		while gemIdx < N and gem[gemIdx][0] <= b:
			heappush(hq, -gem[gemIdx][1])
			gemIdx += 1
		if hq:
			ans += -heappop(hq)
	print(ans)

main()