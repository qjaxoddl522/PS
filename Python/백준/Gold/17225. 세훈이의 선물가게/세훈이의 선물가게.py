import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	A, B, N = map(int, input().split())
	
	# 구간을 전부 seq에 밀어넣고 정렬
	seq = []
	startA = 0; startB = 0
	for _ in range(N):
		t, c, m = input().split()
		start = max(int(t), startA if c == 'B' else startB)
		sep = A if c == 'B' else B
		flag = 0 if c == 'B' else 1

		if sep == 0:
			seq.extend([(start, flag)] * int(m))
		else:
			seq.extend([(i, flag) for i in range(start, start + int(m) * sep, sep)])
		
		if c == 'B':
			startA = start + int(m) * sep
		else:
			startB = start + int(m) * sep
	seq.sort()

	# 정렬된 구간에 번호를 붙여 결과 생성
	resultA = []; resultB = []
	for i in range(len(seq)):
		if seq[i][1] == 0:
			resultA.append(i+1)
		else:
			resultB.append(i+1)
	
	print(len(resultA))
	print(*resultA)
	print(len(resultB))
	print(*resultB)

main()