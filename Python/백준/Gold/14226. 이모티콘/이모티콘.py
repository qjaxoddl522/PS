import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    S = int(input())

    # 입력된 이모티콘의 수, 클립보드에 있는 이모티콘의 수
    visited = [[False] * (S*2) for _ in range(S*2)]
    visited[1][0] = True
    q = deque([(1, 0, 0)])
    while q:
        e, c, t = q.popleft()
        if e == S:
            print(t)
            break

        # 이모티콘 복사
        if e < S and not visited[e][e]:
            q.append((e, e, t+1))
            visited[e][e] = True

        # 이모티콘 붙여넣기
        if c > 0 and e + c < S * 2 and not visited[e+c][c]:
            q.append((e+c, c, t+1))
            visited[e+c][c] = True
        
        # 하나 삭제하기
        if e > 1 and not visited[e-1][c]:
            q.append((e-1, c, t+1))
            visited[e-1][c] = True

main()