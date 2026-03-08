import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    stats = [[] for _ in range(K)]

    for _ in range(N):
        s = list(map(int, input().split()))
        for i in range(K):
            stats[i].append(s[i])
    
    # 각 스탯별로 최고참 뽑아내기
    makers = set()
    for i in range(K):
        maxx = 0
        maxxIdx = -1
        for j in range(N):
            s = stats[i][j]
            if maxx < s:
                maxx = s
                maxxIdx = j
            elif maxx == s:
                maxxIdx = -1
        if maxxIdx >= 0:
            makers.add(maxxIdx)
    print(len(makers))
    
main()