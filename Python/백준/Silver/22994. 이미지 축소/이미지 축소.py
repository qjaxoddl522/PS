import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	ni, mj = map(int, input().split())
	board = [input() for _ in range(ni)]

	def gcd(a, b):
		if b > 0:
			return gcd(b, a%b)
		return a
	
	ii = ni; jj = mj
	for i in range(ni):
		ch = board[i][0]
		cont = 1
		for j in range(1, mj):
			if ch != board[i][j]:
				jj = gcd(jj, cont)
				ch = board[i][j]
				cont = 1
			else:
				cont += 1
	for j in range(mj):
		ch = board[0][j]
		cont = 1
		for i in range(1, ni):
			if ch != board[i][j]:
				ii = gcd(ii, cont)
				ch = board[i][j]
				cont = 1
			else:
				cont += 1
	
	print(ni // ii, mj // jj)
	for i in range(0, ni, ii):
		print(*[board[i][j] for j in range(0, mj, jj)], sep='')

main()