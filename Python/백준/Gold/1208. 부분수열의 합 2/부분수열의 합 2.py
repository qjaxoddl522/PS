import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, S = map(int, input().split())
    ls = list(map(int, input().split()))

    # 값: 개수
    cnt = dict()
    sum = 0
    ans = 0

    def dfs(pos, end):
        nonlocal sum, ans
        if pos == end:
            if end != N:
                if sum not in cnt:
                    cnt[sum] = 0
                cnt[sum] += 1
            elif S-sum in cnt:
                ans += cnt[S-sum]
            return

        dfs(pos+1, end)
        sum += ls[pos]
        dfs(pos+1, end)
        sum -= ls[pos]
    
    dfs(0, N//2)
    dfs(N//2, N)
    if S == 0: ans -= 1
    print(ans)

main()
