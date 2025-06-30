import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	def isWin(t1, t2):
		if dp[t1][t2] != None:
			return dp[t1][t2]
		
		for i in range(3):
			if t1 - b[i] >= 0 and not isWin(t1 - b[i], t2):
				dp[t1][t2] = True
				return True
		
		for j in range(3):
			if t2 - b[j] >= 0 and not isWin(t1, t2 - b[j]):
				dp[t1][t2] = True
				return True
		
		dp[t1][t2] = False
		return False

	b = list(map(int, input().split()))
	# True:A승리 False:B승리
	dp = [[None] * (501) for _ in range(501)]

	for _ in range(5):
		k1, k2 = map(int, input().split())
		print('A' if isWin(k1, k2) else 'B')

main()