import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	dancing = {'ChongChong'}
	for _ in range(N):
		n1, n2 = input().split()
		if n1 in dancing:
			dancing.add(n2)
		elif n2 in dancing:
			dancing.add(n1)
	print(len(dancing))

main()