import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N, K = map(int, input().split())
    S = list(map(int, input().split()))
    # 현재 구간에서의 홀수 개수와 짝수 개수
    odd = 0
    even = 0
    sIdx = 0
    ans = 0
    for e in S:
        if e & 1:
            while sIdx < N and K == odd:
                if S[sIdx] & 1:
                    odd -= 1
                else:
                    even -= 1
                sIdx += 1
            odd += 1
        else:
            even += 1
            ans = max(ans, even)
    print(ans)

main()