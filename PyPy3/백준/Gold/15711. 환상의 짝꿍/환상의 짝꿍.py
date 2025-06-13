import sys
input = lambda: sys.stdin.readline().rstrip()
MAX = 2 * 1_000_000

def main():
	isPrime = bytearray(b'\x01') * (MAX + 1)
	isPrime[0] = isPrime[1] = 0
	for i in range(2, int(MAX**0.5) + 1):
		if isPrime[i]:
			isPrime[i*i: MAX+1: i] = b'\x00' * ((MAX - i*i)//i + 1)
	primes = [i for i, v in enumerate(isPrime) if v]

	def IsPrime(n):
		if n <= MAX:
			return isPrime[n]
		for p in primes:
			if p * p > n:
				break
			if n % p == 0:
				return False
		return True

	for _ in range(int(input())):
		A, B = map(int, input().split())
		# 합이 홀수면 합-2가 소수가 아닌 이상 소수로 나눌 수 없음(하나는 무조건 짝수여야하기 때문)
		if (A + B) % 2 == 1:
			print("YES" if IsPrime(A + B - 2) else "NO")
		# 합이 짝수면 골드바흐의 추측에 의해 범위 내에선 항상 소수인 A + B가 존재함
		else:
			print("YES" if A + B > 3 else "NO")

main()