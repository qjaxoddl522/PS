import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	st = input()
	N = len(st)
	isOff = [c == 'N' for c in st]
	
	ans = 0
	for i in range(N):
		if not isOff[i]:
			ans += 1
			for j in range(i, N, i+1):
				isOff[j] = not isOff[j]
	print(ans)

main()