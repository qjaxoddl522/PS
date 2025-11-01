import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def Main():
    N, L = map(int, input().split())
    ls = list(map(int, input().split()))

    ans = []
    # 인덱스를 넣을 덱
    dq = deque()
    for i, x in enumerate(ls):
        # 넘치는 인덱스 길이 제거
        if dq and dq[0] <= i-L:
            dq.popleft()

        # 추가하기 전에 뒤에서부터 자신보다 최솟값이 아닌 값들의 인덱스 제거
        while dq and ls[dq[-1]] >= x:
            dq.pop()

        dq.append(i)
        ans.append(ls[dq[0]])
    print(*ans)

Main()