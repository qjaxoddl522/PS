import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N, Q, C = map(int, input().split())
    pageCash = [0] + list(map(int, input().split()))
    back = deque()
    cash = 0
    
    def backAppend(n):
        nonlocal cash
        if back and back[-1][0] == n:
            back[-1][1] += 1
        else:
            back.append([n, 1])
        cash += pageCash[n]
    
    def backPop():
        nonlocal cash
        cash -= pageCash[back[-1][0]]
        if back[-1][1] > 1:
            back[-1][1] -= 1
            return back[-1][0]
        return back.pop()[0]
    
    front = deque()
    now = -1
    for _ in range(Q):
        inp = input().split()
        # 뒤로가기
        if inp[0] == 'B':
            if back:
                front.append(now)
                now = backPop()
                cash += pageCash[now]
        # 앞으로가기
        elif inp[0] == 'F':
            if front:
                backAppend(now)
                cash -= pageCash[now]
                now = front.pop()
        # 접속하기
        elif inp[0] == 'A':
            while front:
                cash -= pageCash[front.pop()]
            if now != -1:
                cash -= pageCash[now]
                backAppend(now)
            now = int(inp[1])
            cash += pageCash[now]
            while back and cash > C:
                cash -= pageCash[back[0][0]]
                if back[0][1] > 1:
                    back[0][1] -= 1
                else:
                    back.popleft()
        # 압축하기
        elif inp[0] == 'C':
            for i in range(len(back)):
                cash -= pageCash[back[i][0]] * (back[i][1] - 1)
                back[i][1] = 1
    
    print(now)
    if not back:
        print(-1)
    else:
        for i in range(len(back)-1, -1, -1):
            for j in range(back[i][1]):
                print(back[i][0], end=' ')
        print()
    if not front:
        print(-1)
    else:
        for i in range(len(front)-1, -1, -1):
            print(front[i], end=' ')

main()