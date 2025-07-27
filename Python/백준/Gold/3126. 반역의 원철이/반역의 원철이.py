import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	"""
	원래 도착지를 구하고, 도착지에서부터 방향을 더할 때마다 회전시키며 도작지를 구하기
	각 회전마다 도착지를 O(1)로 구할 수 있기 때문에 전체 시간복잡도는 O(N)
	"""
	move = ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1))

	xb, yb, xg, yg = map(int, input().split())
	N = int(input())
	cmd = list(map(int, input()))

	# i개 명령 수행 후 좌표
	prefPos = [(xb, yb)]
	# i번째 명령 직전 방향
	prefDir = [0]
	d = 0
	for c in cmd:
		d = (d + c) & 7
		x, y = prefPos[-1]
		dx, dy = move[d]
		prefPos.append((x + dx, y + dy))
		prefDir.append(d)

	# i+1번째부터 끝까지 방향 r로 이동했을 때의 벡터
	tail = [(0, 0) for _ in range(8)]
	
	ansPow = (prefPos[-1][0] - xg) ** 2 + (prefPos[-1][1] - yg) ** 2

	for i in range(N-1, -1, -1):
		baseX, baseY = prefPos[i]
		baseDir = prefDir[i]
		for d_new in range(8):
			# 기존 명령 생략
			if d_new == cmd[i]:
				continue

			# 바꿔서 이동할 방향
			newDir = (baseDir + d_new) % 8
			# 그 다음 구간 이동량
			stepX, stepY = move[newDir]
			sufX, sufY = tail[newDir]

			nx = baseX + stepX + sufX
			ny = baseY + stepY + sufY

			distPow = (nx - xg) ** 2 + (ny - yg) ** 2
			ansPow = min(ansPow, distPow)

		newTail = [(0, 0) for _ in range(8)]
		c = cmd[i]
		for r in range(8):
			nd = (r + c) % 8
			sx, sy = tail[nd]
			dx, dy = move[nd]
			newTail[r] = (dx + sx, dy + sy)
		tail = newTail

	print(ansPow ** 0.5)

main()