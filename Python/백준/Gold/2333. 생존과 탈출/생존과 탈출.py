import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	TMAX = 1500
	D, G = map(int, input().split())
	box = [list(map(int, input().split())) for _ in range(G)]
	box.sort()
	
	# dp[시간][현재 높이] = 최대 생존 시간
	dp = [[-1] * (D+1) for _ in range(TMAX+2)]
	dp[0][0] = 10
	idx = 0
	for t in range(TMAX+1):
		base = dp[t][:]
		while idx < G and box[idx][0] == t:
			eat, addH = box[idx][1], box[idx][2]
			for h in range(D+1):
				if base[h] < t:
					continue
				# 먹기
				deadline = base[h] + eat
				if dp[t][h] < deadline:
					dp[t][h] = deadline
				# 쌓기
				nh = min(D, h + addH)
				if dp[t][nh] < base[h]:
					dp[t][nh] = base[h]
			idx += 1
			base = dp[t][:]
		
		if dp[t][D] >= t:
			print(t)
			return
		
		# 시간의 흐름
		for h in range(D+1):
			if dp[t][h] >= t:
				if dp[t+1][h] < dp[t][h]:
					dp[t+1][h] = dp[t][h]
	
	# 생존 가능한 최대 시간
	best = 0
	for row in dp:
		for v in row:
			if v > best:
				best = v
	print(best)

main()