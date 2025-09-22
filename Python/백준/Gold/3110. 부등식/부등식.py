import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    B, C, D = map(int, input().split())
    A1, A2 = map(int, input().split())
    E1, E2 = map(int, input().split())

    ans = 0
    if A1 * E2 < A2 * E1:
        iterL = (A1 * C) // A2
        iterR = (E1 * C + E2 - 1) // E2

        L1 = (A1 * B) // A2
        R2 = (E1 * D + E2 - 1) // E2

        for x in range(iterL, iterR):
            R1 = (x * B + C - 1) // C
            L2 = (x * D) // C

            cntB = R1 - L1 - 1
            if cntB < 0: cntB = 0

            cntD = R2 - L2 - 1
            if cntD < 0: cntD = 0

            ans += cntB * cntD

    print(ans)

main()