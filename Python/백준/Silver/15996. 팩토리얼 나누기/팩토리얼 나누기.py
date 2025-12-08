import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, A = map(int, input().split())
    ans = 0
    a = A
    while a <= N:
        ans += N // a
        a *= A
    print(ans)

main()