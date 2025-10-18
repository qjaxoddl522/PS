import sys
input = lambda: sys.stdin.readline().rstrip()

def Main():
    MOD = 1_000_000
    N = int(input())
    prev = [[0] * 3 for _ in range(2)]
    prev[0][0] = 1
    for _ in range(1, N+1):
        # new[지각횟수(0, 1)][연속 결석일 수(0, 1, 2)]
        new = [[0]*3 for _ in range(2)]
        for l in range(2):
            prevTotal = sum(prev[l])
            # 출석
            new[l][0] = (new[l][0] + prevTotal) % MOD
            # 지각
            if l + 1 < 2:
                new[l+1][0] = (new[l+1][0] + prevTotal) % MOD
            # 결석
            for a in range(2):
                new[l][a+1] += (new[l][a+1] + prev[l][a]) % MOD
        prev = new[:]

    ans = sum(sum(row) for row in prev) % MOD
    print(ans)

Main()