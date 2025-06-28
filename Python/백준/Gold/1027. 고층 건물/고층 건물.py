import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	height = list(map(int, input().split()))

	# 각 건물이 볼 수 있는 다른 건물의 수
	sight = [0] * N
	for i in range(N):
		for j in range(i+1, N):
			a = (height[j] - height[i]) / (j - i)
			for k in range(i+1, j):
				if a * (k - i) <= height[k] - height[i]:
					break
			else:
				sight[i] += 1
				sight[j] += 1
	print(max(sight))

main()