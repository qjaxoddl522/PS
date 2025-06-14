import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, M, Q = map(int, input().split())
	# 개수, 입력데이터 번호... , 가중치..., 편향값
	secure = [list(map(int, input().split())) for _ in range(M)]
	# 가중치..., 편향값
	printer = list(map(int, input().split()))

	# 각 항목의 가중치 합과 곱을 미리 구하기
	mult = [0] * (N+1)
	plus = 0

	for i in range(M):
		S = secure[i]
		n = S[0]
		for j in range(1, n+1):
			mult[S[j]] += S[n+j] * printer[i]
		plus += S[-1] * printer[i]
	plus += printer[M]
	
	for _ in range(Q):
		A = list(map(int, input().split()))
		result = plus
		for i in range(1, N+1):
			result += A[i-1] * mult[i]
		print(result)

main()