import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	A = list(map(int, input().split()))
	oper = list(map(int, input().split()))

	maxx, minn = -float('inf'), float('inf')
	def calc(val, idx):
		nonlocal maxx, minn
		if idx == N:
			maxx = max(maxx, val)
			minn = min(minn, val)
			return
		
		for i in range(4):
			if oper[i] > 0:
				oper[i] -= 1
				if i == 0:
					calc(val + A[idx], idx + 1)
				elif i == 1:
					calc(val - A[idx], idx + 1)
				elif i == 2:
					calc(val * A[idx], idx + 1)
				elif i == 3:
					if val < 0:
						calc(-(-val // A[idx]), idx + 1)
					else:
						calc(val // A[idx], idx + 1)
				oper[i] += 1
	calc(A[0], 1)
	print(maxx)
	print(minn)

main()