import sys
from collections import deque
input = sys.stdin.readline

DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    owner = [[-1] * N for _ in range(N)]   # 땅·바다의 소유 섬 ID
    dist  = [[-1] * N for _ in range(N)]   # 바다로 퍼진 거리(해안 = 0)

    q = deque()
    idx = 0  # 섬 번호

    # 섬 라벨링
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1 and owner[r][c] == -1:
                idx += 1
                owner[r][c] = idx
                land = deque([(r, c)])
                while land:
                    x, y = land.popleft()
                    edge = False
                    for dx, dy in DIR:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if board[nx][ny] == 1 and owner[nx][ny] == -1:
                                owner[nx][ny] = idx
                                land.append((nx, ny))
                            elif board[nx][ny] == 0:
                                edge = True
                    if edge:
                        q.append((x, y))
                        dist[x][y] = 0

    # 바다 채우기
    answer = 10**9
    while q:
        x, y = q.popleft()
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                # 아직 아무 섬도 차지 안 한 바다라면 진출
                if board[nx][ny] == 0 and dist[nx][ny] == -1:
                    owner[nx][ny] = owner[x][y]
                    dist[nx][ny]  = dist[x][y] + 1
                    q.append((nx, ny))
                # 이미 다른 섬이 먼저 차지한 바다(또는 해안)를 만남
                elif owner[nx][ny] != owner[x][y]:
                    answer = min(answer, dist[x][y] + dist[nx][ny])

    print(answer)

main()
