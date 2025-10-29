import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def Main():
    A, B = map(int, input().split())
    ans = 0
    L = int(math.log10(B)) + 1
    def backtrack(n):
        nonlocal ans
        l = int(math.log10(n)) + 1
        if L < l:
            return
        if A <= n <= B:
            ans += 1
        backtrack(n*10+4)
        backtrack(n*10+7)
    
    backtrack(4)
    backtrack(7)
    print(ans)

Main()