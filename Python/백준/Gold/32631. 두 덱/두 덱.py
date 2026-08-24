import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, K = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))

	def getDp(n, prefix):
		# dp[i] = i개의 연속된 원소를 선택할 때 최소 합
		dp = [float('inf')] * (n + 1)
		dp[0] = 0
		
		for length in range(1, n + 1):
			for start in range(1, n - length + 2):
				end = start + length - 1
				subarraySum = prefix[end] - prefix[start - 1]
				dp[length] = min(dp[length], subarraySum)
		
		return dp

	prefixA = [0]
	prefixB = [0]
	for i in range(N):
		prefixA.append(prefixA[-1] + A[i])
		prefixB.append(prefixB[-1] + B[i])
    
	# 각 배열에서 i개의 연속된 원소를 선택할 때 최소 합
	dpA = getDp(N, prefixA)
	dpB = getDp(N, prefixB)
	
	# A에서 i개, B에서 j개
	answer = float('inf')
	for i in range(N + 1):
		j = 2 * N - K - i
		if 0 <= j <= N:
			answer = min(answer, max(dpA[i], dpB[j]))
	print(answer)

main()