import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	S = list(input())
	for i in range(len(S)):
		S[i] = S[i].upper() if ord(S[i]) >= 97 else S[i].lower()
	print(*S, sep='')

main()