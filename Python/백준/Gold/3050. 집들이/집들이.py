import sys
input = lambda: sys.stdin.readline().rstrip()

def Main():
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    
    # 세로 누적합 구하기
    colPrefix = [[0] * (N+1) for _ in range(M)]
    for c in range(M):
        for r in range(1, N+1):
            colPrefix[c][r] = colPrefix[c][r-1] + (1 if board[r-1][c] == '.' else 0)
    
    ans = 0
    for top in range(1, N+1):
        for bot in range(top, N+1):
            # 최대 연속 가로 구간 길이
            run = 0
            for c in range(M):
                if colPrefix[c][bot] - colPrefix[c][top-1] == (bot-top+1):
                    run += 1
                    ans = max(ans, 2 * ((bot-top+1) + run))
                else:
                    run = 0
    print(ans-1)

Main()