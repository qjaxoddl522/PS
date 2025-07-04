import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	MOD = 1_000_000_007
	N = int(input())

	# [직전 높이][높이2 포함 여부][연속 선인장 수]
	prev = [[[0] * 3 for _ in range(2)] for _ in range(3)]
	prev[0][0][0] = 1
	prev[1][0][1] = 1
	prev[2][1][1] = 1
	for _ in range(N-2):
		next = [[[0] * 3 for _ in range(2)] for _ in range(3)]
		for i in range(3):
			for j in range(2):
				for k in range(3):
					now = prev[i][j][k]
					if now == 0:
						continue
					
					# 다음 높이
					for iNext in range(3):
						if i == 2 and iNext == 2:
							continue
						
						if iNext == 0:
							count = 0
						else:
							count = (k + 1) if i > 0 else 1
							if count > 2:
								continue

						jNext = j or (iNext == 2)
						next[iNext][jNext][count] = (next[iNext][jNext][count] + now) % MOD
		prev = next
	
	# 높이2를 사용한 모든 합
	result = sum(prev[h][1][c] for h in range(3) for c in range(3)) % MOD
	print(result if N > 1 else 0)

main()