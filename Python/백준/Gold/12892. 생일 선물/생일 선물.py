import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, D = map(int, input().split())
	gift = [list(map(int, input().split())) for _ in range(N)]
	gift.sort()
	
	ans = 0
	manjok = 0
	s = 0
	for e in range(N):
		manjok += gift[e][1]
		while gift[e][0] - gift[s][0] >= D:
			manjok -= gift[s][1]
			s += 1
		ans = max(ans, manjok)
	print(ans)

main()