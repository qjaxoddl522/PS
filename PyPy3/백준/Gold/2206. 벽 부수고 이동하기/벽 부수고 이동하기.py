from collections import deque
import sys
input = sys.stdin.readline

mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

def bfs():
    while q:
        x, y, wall = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][wall]
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if 0<=nx<N and 0<=ny<M:
                if wall == 0: #아직 안부숨
                    if mp[nx][ny] == 1 and visited[nx][ny][1] == 0:
                        q.append((nx, ny, 1)) #벽 부수고 이동
                        visited[nx][ny][1] = visited[x][y][0] + 1
                    elif mp[nx][ny] == 0 and visited[nx][ny][0] == 0:
                        q.append((nx, ny, 0)) #벽 안부수고 이동
                        visited[nx][ny][0] = visited[x][y][0] + 1
                else: #벽부숨
                    if mp[nx][ny] == 0 and visited[nx][ny][1] == 0:
                        q.append((nx, ny, 1))
                        visited[nx][ny][1] = visited[x][y][1] + 1
    return -1

N, M = map(int, input().split())
mp = [list(map(int, list(input().rstrip())))for _ in range(N)]

#visited[][][0]안부순 경로 visited[][][1]부순 경로
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

q = deque()
q.append((0, 0, 0))
print(bfs())
