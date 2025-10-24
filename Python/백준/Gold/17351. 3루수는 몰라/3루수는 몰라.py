import sys
input = lambda: sys.stdin.readline().rstrip()

def Main():
    STR = "MOLA"
    L = len(STR)
    N = int(input())
    board = [input() for _ in range(N)]

    # 최대 MOLA의 수
    prev = [0] * N
    for i in range(N):
        now = [0] * N
        for j in range(N):
            s = STR.find(board[i][j])
            # 이전에서 이을 수 있는 최대 연속 문자
            now[j] = max(now[j-1] - (now[j-1] % L), prev[j] - (prev[j] % L))
            # 문자열 시작점
            if s == 0:
                now[j] += 1
            elif s > 0:
                # 왼쪽에서 잇기
                if now[j-1] % L == s:
                    now[j] = max(now[j], now[j-1] + 1)
                # 위에서 잇기
                if prev[j] % L == s:
                    now[j] = max(now[j], prev[j] + 1)
        prev = now[:]
    print(now[N-1] // L)

Main()