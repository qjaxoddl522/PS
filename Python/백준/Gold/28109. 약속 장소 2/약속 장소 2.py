import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, K = map(int, input().split())
	s = input().strip()
	S = [ord(c) - ord('A') for c in s]
	
	# 원문의 앞부분
	for i in range(N):
		if S[i] >= K:
			S[i] = K-1
			print(''.join(chr(x + 65) for x in S))
			return
		else:
			K -= S[i]
	
	# 원문
	if K == 1:
		print(s)
		return
	K -= 1

	# 원문의 뒷부분
	for i in range(N-1, -1, -1):
		if 25 - S[i] >= K:
			S[i] += K
			print(''.join(chr(x + 65) for x in S))
			return
		else:
			K -= 25 - S[i]

	print(-1)

main()