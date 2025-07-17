import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	X, Y = map(int, input().split())
	if X == Y:
		# 11 => 00, 02, 22, 20
		print(7)
		print(-X, X)
		print(0, X*2)
		print(X, X*3)
		print(X*2, X*2)
		print(X*3, X)
		print(X*2, 0)
		print(X, X)
	elif X == 0 or Y == 0:
		A = X if Y == 0 else Y
		# 10 => 00, 11, 20, 1-1
		print(7)
		print(0, A)
		print(A, A)
		print(A*2, A)
		print(A*2, 0)
		print(A*2, -A)
		print(A, -A)
		print(A, 0)
	else:
		## 21 => 00, 1-1, 3-1, 40, 42, 33, 13, 02
		print(15)
		print(-Y, -X)
		print(X-Y, Y-X)
		print(X, Y-X-X)
		print(X+Y, Y-X)
		print(X+X+Y, -X)
		print(X+X, 0)
		print(X+X+X, Y)
		print(X+X, Y+Y)
		print(X+X+Y, Y+X+Y)
		print(X+Y, Y+X)
		print(X, Y+X+X)
		print(X-Y, Y+X)
		print(-Y, Y+X+Y)
		print(0, Y+Y)
		print(X, Y)

main()