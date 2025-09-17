import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    T = int(input())
    out = []
    for _ in range(T):
        N = int(input())

        if N % 4 == 2:
            out.append("IMPOSSIBLE")
            continue

        r = math.isqrt(N)
        found = False
        for x in range(r, 0, -1):
            if N % x: 
                continue
            y = N // x
            if ((x ^ y) & 1):
                continue
            a = (x + y) // 2
            b = (y - x) // 2
            out.append(f"{b} {a}")
            found = True
            break

        if not found:
            out.append("IMPOSSIBLE")

    print("\n".join(out))

main()