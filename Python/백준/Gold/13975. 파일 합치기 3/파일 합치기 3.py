import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

def main():
	for _ in range(int(input())):
		N = int(input())
		A = list(map(int, input().split()))
		heapq.heapify(A)
		
		result = 0
		while len(A) > 1:
			a = heapq.heappop(A); b = heapq.heappop(A)
			result += a + b
			heapq.heappush(A, a+b)
		print(result)

main()