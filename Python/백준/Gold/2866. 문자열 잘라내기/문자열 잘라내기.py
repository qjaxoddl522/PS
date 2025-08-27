import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	R, C = map(int, input().split())
	S = [list(input()) for _ in range(R)]
	
	overlap = set()
	prevString = []
	
	for r in range(R-1, -1, -1):
		# 중복이 있는가
		isOverlap = False
		prevStringWait = []
		for c in range(C):
			if prevString:
				newStr = S[r][c] + prevString[c]
			else:
				newStr = S[r][c]
			if newStr in overlap:
				isOverlap = True
			else:
				overlap.add(newStr)
			prevStringWait.append(newStr)
		if not isOverlap:
			print(r)
			break
		prevString = prevStringWait
		overlap = set()
	else:
		print(0)

main()