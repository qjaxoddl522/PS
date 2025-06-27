import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())

	def bt(a, n):
		if n < N and a == 1:
			return
		if n == 1:
			result.append(a)
			return
		
		if ((a-1)/3) % 1 == 0 and ((a-1)//3) & 1:
			bt((a-1)//3, n-1)
		bt(a*2, n-1)
		
	result = []
	bt(1, N)
	print(len(result))
	print(*sorted(result), sep='\n')

main()