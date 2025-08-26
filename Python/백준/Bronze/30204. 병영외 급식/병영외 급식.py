import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, X = map(int, input().split())
	S = sum(list(map(int, input().split())))
	print(0 if S % X else 1)

main()