import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, Q, U, V = map(int, input().split())
	K = [None] + list(map(int, input().split()))
	# K 누적합
	kSum = [0] * (N+1)
	# 수식 결과값
	func = [0] * (N+1)

	for i in range(N):
		kSum[i+1] = kSum[i] + K[i+1]
		func[i+1] = U * kSum[i+1] + V * (i+1)

	for _ in range(Q):
		C, A, B = map(int, input().split())
		if C == 0:
			left = float('inf')
			right = -float('inf')
			for i in range(A, B+1):
				left = min(left, func[i-1])
				right = max(right, func[i] - left)
			print(right - V)
		else:
			diff = B - K[A]
			for i in range(A, N+1):
				kSum[i] += diff
				func[i] += U * diff
			K[A] = B

main()