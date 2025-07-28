import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = 20
SIZE = MAX + 1

dp = [[[0]*SIZE for _ in range(SIZE)] for __ in range(SIZE)]
for a in range(SIZE):
    for b in range(SIZE):
        for c in range(SIZE):
            if a == 0 or b == 0 or c == 0:
                dp[a][b][c] = 1
            elif a < b < c:
                dp[a][b][c] = (dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c])
            else:
                dp[a][b][c] = (dp[a-1][b][c] +dp[a-1][b-1][c] +dp[a-1][b][c-1] -dp[a-1][b-1][c-1])

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        ans = 1
    elif a > MAX or b > MAX or c > MAX:
        ans = dp[MAX][MAX][MAX]
    else:
        ans = dp[a][b][c]

    print(f"w({a}, {b}, {c}) = {ans}")