import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop, heapify

def main():
    info = dict()
    ans = 0
    for _ in range(int(input())):
        inp = input().split()
        cmd = int(inp[0])
        name = inp[1]
        if cmd == 1:
            ls = [-int(x) for x in inp[3:]]
            if name not in info:
                info[name] = ls
            else:
                for i in ls:
                    heappush(info[name], i)
        elif cmd == 2:
            n = int(inp[2])
            while name in info and info[name] and n > 0:
                ans -= heappop(info[name])
                n -= 1
    print(ans)

main()