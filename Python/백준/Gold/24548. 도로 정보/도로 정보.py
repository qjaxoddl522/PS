import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	road = input()
	
	result = 0
	# pattern에 같은 기록을 가지는 prefix 수열의 수만큼 결과에 더함
	pattern = {(0, 0, 0, 0):1}
	# T, G, F, P
	prefix = [0, 0, 0, 0]
	for i in range(1, N+1):
		if road[i-1] == 'T':
			prefix[0] = (prefix[0] + 1) % 3
		elif road[i-1] == 'G':
			prefix[1] = (prefix[1] + 1) % 3
		elif road[i-1] == 'F':
			prefix[2] = (prefix[2] + 1) % 3
		elif road[i-1] == 'P':
			prefix[3] = (prefix[3] + 1) % 3
		
		tp = tuple(prefix)
		if tp in pattern:
			result += pattern[tp]
			pattern[tp] += 1
		else:
			pattern[tp] = 1
	
	print(result)

main()