from collections import deque
def solution(x, y, n):
    visited = [False] * (y+1)
    visited[x] = True
    dq = deque([(x, 0)])
    while dq:
        xx, num = dq.popleft()
        if xx == y:
            return num
        
        for next in (xx+n, xx*2, xx*3):
            if next <= y and not visited[next]:
                dq.append((next, num+1))
                visited[next] = True
    return -1