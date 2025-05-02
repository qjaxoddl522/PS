import sys, math
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

def main():
    N, K = map(int, input().split())
    ls = list(map(int, input().split()))

    prefix = defaultdict(int)
    prefix[0] = 1
    s = answer = 0
    for x in ls:
        s += x
        answer += prefix[s-K]
        prefix[s] += 1
    print(answer)

main()