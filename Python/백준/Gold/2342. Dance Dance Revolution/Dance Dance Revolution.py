import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	note = [0] + list(map(int, input().split()))
	N = len(note) - 1

	def GetEnergy(now, new):
		if now == new:
			return 1
		if now == 0 or new == 0:
			return 2
		sub = abs(now - new)
		if sub == 1 or sub == 3:
			return 3
		return 4

	# prev[i] = 해당 노트를 밟지 않은 나머지 발의 위치가 i일 때 드는 최소 힘
	prev = [float('inf')] * 5
	prev[0] = 0
	now = [float('inf')] * 5
	for i in range(1, N):
		now = [float('inf')] * 5
		for j in range(5):
			if j != note[i]:
				# 이전 노트의 발을 옮긴 경우
				now[j] = min(now[j], prev[j] + GetEnergy(note[i-1], note[i]))
			if note[i-1] != note[i]:
				# 이전 노트에서 밟지 않은 나머지 발을 옮긴 경우
				now[note[i-1]] = min(now[note[i-1]], prev[j] + GetEnergy(j, note[i]))
		prev = now
		#print(now, note[i])
	ans = min(now)
	print(ans if ans < float('inf') else 0)

main()