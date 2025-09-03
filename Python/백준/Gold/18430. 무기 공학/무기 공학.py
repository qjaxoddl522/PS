import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, M = map(int, input().split())
	K = [list(map(int, input().split())) for _ in range(N)]

	used = [[False] * M for _ in range(N)]
	ans = 0
	def bt(idx, power):
		nonlocal ans
		r, c = idx // M, idx % M
		if idx == N * M:
			ans = max(ans, power)
			return
		if used[r][c]:
			bt(idx+1, power)
			return

		# 현재 위치를 중심으로 4방향 만들기
		used[r][c] = True
		power += K[r][c] * 2
		if r+1 < N and c+1 < M and not used[r+1][c] and not used[r][c+1]:
			used[r+1][c] = True
			used[r][c+1] = True
			bt(idx+2, power + K[r+1][c] + K[r][c+1])
			used[r+1][c] = False
			used[r][c+1] = False
		if r+1 < N and c-1 >= 0 and not used[r+1][c] and not used[r][c-1]:
			used[r+1][c] = True
			used[r][c-1] = True
			bt(idx+1, power + K[r+1][c] + K[r][c-1])
			used[r+1][c] = False
			used[r][c-1] = False
		if r-1 >= 0 and c-1 >= 0 and not used[r-1][c] and not used[r][c-1]:
			used[r-1][c] = True
			used[r][c-1] = True
			bt(idx+1, power + K[r-1][c] + K[r][c-1])
			used[r-1][c] = False
			used[r][c-1] = False
		if r-1 >= 0 and c+1 < M and not used[r-1][c] and not used[r][c+1]:
			used[r-1][c] = True
			used[r][c+1] = True
			bt(idx+2, power + K[r-1][c] + K[r][c+1])
			used[r-1][c] = False
			used[r][c+1] = False
		power -= K[r][c] * 2
		used[r][c] = False

		# 혹은 현재 위치를 선택하지 않고 진행
		bt(idx+1, power)
	
	bt(0, 0)
	print(ans)

main()