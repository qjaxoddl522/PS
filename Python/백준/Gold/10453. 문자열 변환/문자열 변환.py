import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        A, B = input().split()
        N = len(A)
        idxA, idxB = 0, 0
        ans = 0
        while idxA < N:
            if A[idxA] == 'b':
                while idxB < N and B[idxB] != 'b':
                    idxB += 1
                ans += abs(idxA - idxB)
                idxB += 1
            idxA += 1
        print(ans if idxA == idxB else -1)

main()