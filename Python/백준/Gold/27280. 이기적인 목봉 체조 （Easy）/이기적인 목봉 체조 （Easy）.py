import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, M = map(int, input().split())
	hs = [list(map(int, input().split())) for _ in range(N)]
	
	# dp[i][j] = i부터 j까지 그룹일 때 드는 (키, 무게)
	dp = [[0]*N for _ in range(N)]
	for l in range(N):
		maxH = -1
		sumW = 0
		for r in range(l, N):
			h, w = hs[r]
			if h > maxH:
				maxH = h
				sumW = w
			elif h == maxH:
				sumW += w
			dp[l][r] = sumW

	# f[i][j] = 앞에서 j까지 i개 그룹으로 나눴을 때 최대합
	f = [[0] * N for _ in range(M+1)]
	cut = [[-1] * N for _ in range(M+1)]

	for r in range(N):
		f[1][r] = dp[0][r]
		cut[1][r] = 0

	for m in range(2, M+1):
		for r in range(m-1, N):
			best = 0
			bestL = -1
			for l in range(m-1, r+1):
				cand = f[m-1][l-1] + dp[l][r]
				if cand > best:
					best = cand
					bestL = l
			f[m][r] = best
			cut[m][r] = bestL

	print(f[M][N-1])

main()