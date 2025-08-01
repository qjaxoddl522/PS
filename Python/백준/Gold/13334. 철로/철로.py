import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def main():
	"""
	d보다 긴 구간은 고려하지 않기
	시작 위치 순서대로 구간 정렬
	첫 시작 위치 + d의 구간 안에 있는 시작 위치까지 순회하여 끝 위치를 힙큐에 입력
	현재 위치 + d보다 작을 동안 끝 위치 힙큐에서 꺼내면서 현재 포함구간 힙큐에 입력
	현재 포함구간의 길이를 정답과 비교 및 갱신
	"""
	n = int(input())
	originInfo = [list(map(int, input().split())) for _ in range(n)]
	d = int(input())

	info = []
	for h, o in originInfo:
		if h > o:
			h, o = o, h
		if o - h <= d:
			info.append((h, o))
	info.sort()
	
	ans = 0
	# 현재 포함하고 있는 구간
	now = []
	# now에 들어갈 수 있는지 확인하는 끝구간 (끝, 시작)
	endQueue = []
	startIdx = 0
	for s, _ in info:
		while now and now[0] < s:
			heappop(now)
		while startIdx < len(info) and info[startIdx][0] <= s + d:
			heappush(endQueue, (info[startIdx][1], info[startIdx][0]))
			startIdx += 1
		while endQueue and endQueue[0][0] <= s + d:
			heappush(now, heappop(endQueue)[1])
		ans = max(ans, len(now))
	print(ans)

main()