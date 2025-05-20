import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    R, C = map(int, input().split())
    N = int(input())
    ls = sorted(list(map(int, input().split())))

    ans = 0
    prev = [0] * C
    c = 0
    for t in ls:
        if prev[c] < t:
            ans += 1
            prev[c] = t
            c += 1
            if c == C:
                c -= C
                R -= 1
                if R == 0:
                    break
    print(ans)

main()