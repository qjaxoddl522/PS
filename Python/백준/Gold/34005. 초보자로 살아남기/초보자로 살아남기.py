import sys
input = lambda: sys.stdin.readline().rstrip()

MAX_T = 600
MAX_SP = 100
# 후 딜레이 끝난 쿨타임
C3_LEN, C4_LEN = 2, 7

def main():
	A, B, C, P = map(int, input().split())

	# 스킬 쿨타임은 후딜레이 이후 기준이므로, 기본 공격과 해머링은 쿨타임이 없음
	# dp[시간][sp][스트라이크 쿨타임][박치기 쿨타임] = 최대 누적 데미지
	dp = [[[[-1] * C4_LEN for _ in range(C3_LEN)]
		for _ in range(MAX_SP + 1)] for _ in range(MAX_T + 1)]
	# 1초부터 시작
	dp[1][MAX_SP][0][0] = 0

	for t in range(1, MAX_T + 1):
		for sp in range(MAX_SP + 1):
			for c3 in range(C3_LEN):
				for c4 in range(C4_LEN):
					dmg = dp[t][sp][c3][c4]
					if dmg < 0:
						continue

					# 기본 공격
					nsp = min(sp + 1, MAX_SP)
					n3 = max(c3 - 1, 0)
					n4 = max(c4 - 1, 0)
					ndmg = dmg + 100
					if ndmg >= P:
						print(t)
						return
					if t + 1 <= MAX_T:
						dp[t + 1][nsp][n3][n4] = max(dp[t + 1][nsp][n3][n4], ndmg)

					# 해머링
					nsp = min(sp + 8, MAX_SP)
					n3 = max(c3 - 1, 0)
					n4 = max(c4 - 1, 0)
					ndmg = dmg + A
					if ndmg >= P:
						print(t)
						return
					if t + 1 <= MAX_T:
						dp[t + 1][nsp][n3][n4] = max(dp[t + 1][nsp][n3][n4], ndmg)

					# 스트라이크
					if sp >= 10 and c3 == 0:
						ndmg = dmg + B
						if ndmg >= P:
							print(t)
							return
						nsp = sp - 8
						n3 = 1
						n4 = max(c4 - 2, 0)
						if t + 2 <= MAX_T:
							dp[t + 2][nsp][n3][n4] = max(dp[t + 2][nsp][n3][n4], ndmg)

					# 박치기
					if sp >= 10 and c4 == 0:
						ndmg = dmg + C
						if ndmg >= P:
							print(t)
							return
						nsp = sp - 8
						n3 = max(c3 - 2, 0)
						n4 = 6
						if t + 2 <= MAX_T:
							dp[t + 2][nsp][n3][n4] = max(dp[t + 2][nsp][n3][n4], ndmg)
	
	print(-1)

for _ in range(int(input())):
	main()