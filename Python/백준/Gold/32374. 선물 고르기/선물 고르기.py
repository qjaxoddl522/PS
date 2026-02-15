import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_right

def main():
    N, K = map(int, input().split())
    # 선물 중 내 상자보다 작은 상자 수 만큼 제외
    A = sorted(list(map(int, input().split())))[N-K-1:]
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # 다른 사람이 가져간 선물 상자 제외하기 => 남은 것 중 가장 큰 상자가 내거
    Bdict = dict()
    for b in B:
        if not b in Bdict:
            Bdict[b] = 0
        Bdict[b] += 1
    for c in C:
        Bdict[c] -= 1
        if Bdict[c] == 0:
            del Bdict[c]
    # 남은 선물 중 내가 가져갈수 있는 가장 큰 선물 담기
    print(A[bisect_right(A, max(Bdict))-1])

main()