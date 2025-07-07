import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	seq = list(map(int, input().split()))

	# 최소 숫자와 인덱스 파악 및 중복 확인
	m = seq[0]
	mIdx = 0
	visited = {seq[0]}
	for i in range(1, N):
		if seq[i] in visited:
			print(0)
			return
		visited.add(seq[i])
		if m > seq[i]:
			m = seq[i]
			mIdx = i
	
	# 최소가 N보다 크면 전부 교체된 상황이므로 가능
	if m > N:
		print(1)
		return
	
	# 순회하면서 교체된 곤돌라가 아니고 번호 순서가 잘못되었을 경우 불가능
	startIdx = mIdx - m
	for expect in range(1, N+1):
		i = (startIdx + expect) % N
		if seq[i] <= N and seq[i] != expect:
			print(0)
			break
	else:
		print(1)

main()