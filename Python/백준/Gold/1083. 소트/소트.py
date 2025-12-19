import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    ls = list(map(int, input().split()))
    S = int(input())

    for i in range(N):
        # 바꿀 수 있는 최대횟수
        f = min(S, N-i-1)
        # 바꿀 인덱스 찾기
        idx = i
        maxx = ls[i]
        for j in range(i+1, i+f+1):
            if maxx < ls[j]:
                idx = j
                maxx = ls[j]
        change = ls[idx]
        del ls[idx]
        ls.insert(i, change)
        S -= idx - i
    print(*ls)

main()