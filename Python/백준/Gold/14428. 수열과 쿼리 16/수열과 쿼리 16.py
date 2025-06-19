import sys
input = lambda: sys.stdin.readline().rstrip()
import math

MAX = float('inf')

def main():
    def change(idx, value):
        idx += leafLen
        segTree[idx] = (value, idx - leafLen)
        while idx > 1:
            idx //= 2
            if segTree[idx*2][0] <= segTree[idx*2+1][0]:
                segTree[idx] = segTree[idx*2]
            else:
                segTree[idx] = segTree[idx*2+1]
    
    def query(i, j):
        # (현재 인덱스, 현재 인덱스가 포함하고 있는 구간 좌, 우)
        def inner(idx, left, right):
            if left > j or right < i:
                return (MAX, -1)
            if left >= i and right <= j:
                return segTree[idx]
            
            mid = (left + right) // 2
            leftRes = inner(idx*2, left, mid)
            rightRes = inner(idx*2+1, mid+1, right)
            #print(f"left: {left}, {mid}, right: {mid+1}, {right}")
            return leftRes if leftRes[0] <= rightRes[0] else rightRes
        return inner(1, 0, leafLen-1)

    N = int(input())
    leafLen = 2 ** math.ceil(math.log2(N))
    segTree = [(MAX, -1)] * (leafLen*2)

    initList = list(map(int, input().split()))
    for i in range(N):
        segTree[leafLen+i] = (initList[i], i)
    
    for i in range(leafLen-1, 1, -1):
        if segTree[i*2][0] <= segTree[i*2+1][0]:
            segTree[i] = segTree[i*2]
        else:
            segTree[i] = segTree[i*2+1]
    
    for _ in range(int(input())):
        cmd, a, b = map(int, input().split())
        if cmd == 1:
            change(a-1, b)
        elif cmd == 2:
            print(query(a-1, b-1)[1]+1)

main()