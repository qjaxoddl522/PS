import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, K = map(int, input().split())
	# 카드 숫자, 이전 카드의 위치, 다음 카드의 위치, 소유 플레이어 번호
	info = []
	for p in range(1, N+1):
		row = map(int, input().split())
		for a in row:
			info.append([a, (len(info)-1)%(N*K), (len(info)+1)%(N*K), p])
	
	idx = 0
	for _ in range(N*K):
		num, prev, next, player = info[idx]
		info[prev][2] = next
		info[next][1] = prev
		while num > 0:
			idx = info[idx][2]
			num -= 1
	print(player, info[idx][0])

main()