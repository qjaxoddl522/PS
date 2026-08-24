import sys
input = sys.stdin.readline

def safe(x): #퀸이 안전한지 확인
    for i in range(x):
        #같은 행 or 대각선
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

def dfs(st): #(시작 행)
    global ans
    if st == N: #마지막까지 탐색
        ans += 1
        return

    for i in range(N): #열 탐색
        row[st] = i
        if safe(st):
            dfs(st+1)

N = int(input().rstrip())

row = [0] * N #row[i] = j: i행 j열에 퀸이 존재
ans = 0
dfs(0)

print(ans)
