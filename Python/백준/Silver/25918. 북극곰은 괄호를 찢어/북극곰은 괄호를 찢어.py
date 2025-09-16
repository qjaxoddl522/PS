import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	S = list(input())

	ans = 0
	sto = 0
	stx = 0
	for s in S:
		if s == '(':
			if stx > 0:
				stx -= 1
			else:
				sto += 1
		elif s == ')':
			if sto > 0:
				sto -= 1
			else:
				stx += 1
		ans = max(ans, sto, stx)
	print(ans if sto == 0 and stx == 0 else -1)

main()