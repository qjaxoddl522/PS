import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heapify, heappop, heappush

def main():
    N, H, T = map(int, input().split())
    height = [-int(input()) for _ in range(N)]
    heapify(height)
    
    count = 0
    while -height[0] >= H and count < T:
        heappush(height, min(-1, -(-heappop(height)//2)))
        count += 1
    
    if -height[0] < H:
        print("YES")
        print(count)
    else:
        print("NO")
        print(-height[0])

main()