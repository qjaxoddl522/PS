import sys
input  = sys.stdin.readline
t = int(input())

dy = [-1,1,0,0] # 행   위 , 아래, 고정 , 고정
dx = [0,0,-1,1] # 열  고정, 고정, 왼쪽 , 오른쪽
# (dx,dy) -> (x,y)의 좌표를 조정
def bfs(graph,x,y):
    q = [(x,y)] # q에 입력받은 좌표를 추가
    graph[x][y] = 0 # 입력받은 좌표 값 변경(배추제거  1 -> 0)
    while q:
        x,y = q.pop(0) # q에 넣은 값을 제거
        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 1<=nx<=m and 1<=ny<=n and graph[nx][ny] == 1: # 배추가 있으면 
                q.append((nx,ny)) # 큐에 좌표를 추가하고
                graph[nx][ny] = 0 # 방문처리
for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0]*(n+1) for _ in range(m+1)] 
    cnt = 0
    for _ in range(k):
        x,y = map(int, input().split())
        x = x+1
        y = y+1
        graph[x][y] = 1 # 입력받은 좌표에 배추를 심음
    
    for i in range(1,m+1): # i는 행의 개수, j는 열의 개수
        for j in range(1,n+1): # 모든 좌표를 둘러봄
            if graph[i][j] == 1: # (i,j)좌표에 배추가 있으면 bfs함수 호출
                bfs(graph, i,j) 
                cnt +=1 # bfs가 근처 배추밭을 전부 방문처리하면 카운트 +1

    print(cnt)