import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
from bisect import bisect_right

def main():
    N, C = map(int, input().split())
    weight = list(map(int, input().split()))

    hap = 0
    def GetHap(pos, end, result:defaultdict):
        nonlocal hap
        if pos == end:
            if hap <= C:
                result[hap] += 1
            return

        GetHap(pos+1, end, result)
        hap += weight[pos]
        GetHap(pos+1, end, result)
        hap -= weight[pos]
    
    resLeft, resRight = defaultdict(int), defaultdict(int)
    GetHap(0, N//2, resLeft)
    GetHap(N//2, N, resRight)

    # 오른쪽 값들 누적합
    rightKeys = sorted(resRight.keys())
    pref = []
    s = 0
    for k in rightKeys:
        s += resRight[k]
        pref.append(s)

    ans = 0
    for l, cntL in resLeft.items():
        idx = bisect_right(rightKeys, C - l) - 1
        if idx >= 0:
            ans += cntL * pref[idx]
    print(ans)

main()