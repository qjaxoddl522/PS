import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	left = int(input())
	cnt = [0] * 10

	# 현재 자릿수
	digit = 1
	# 현재 커서의 오른쪽 수
	right = 0
	while left > 0:
		n = left % 10
		left //= 10

		# 000... 의 경우를 제거하기
		cnt[0] -= digit
		for i in range(n):
			cnt[i] += (left + 1) * digit
		cnt[n] += left * digit + right + 1
		for i in range(n+1, 10):
			cnt[i] += left * digit
		
		# 자릿수 이동
		right += n * digit
		digit *= 10
	
	print(*cnt)

main()