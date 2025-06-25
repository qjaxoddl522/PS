import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	S = []; W = []
	for _ in range(N):
		s, w = map(int, input().split())
		S.append(s)
		W.append(w)
	
	result = 0
	def bt(n, broke):
		nonlocal result
		if n == N or broke >= N-1:
			result = max(result, broke)
			return
		if S[n] <= 0:
			bt(n+1, broke)
			return
		
		for i in range(N):
			if i != n and S[i] > 0:
				broken = broke
				S[i] -= W[n]
				if S[i] <= 0:
					broken += 1
				S[n] -= W[i]
				if S[n] <= 0:
					broken += 1
				bt(n+1, broken)
				S[i] += W[n]
				S[n] += W[i]
	
	bt(0, 0)
	print(result)

main()