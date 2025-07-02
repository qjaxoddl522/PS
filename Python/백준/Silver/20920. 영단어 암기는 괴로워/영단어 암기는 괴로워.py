import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N, M = map(int, input().split())

	count = dict()
	for _ in range(N):
		word = input()
		if len(word) < M:
			continue
		
		if word not in count:
			count[word] = 0
		count[word] += 1
	
	ls = list(count.keys())
	ls.sort(key= lambda x: (-count[x], -len(x), x))
	print(*ls, sep='\n')

main()