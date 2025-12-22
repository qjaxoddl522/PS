import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = [0] * (N+1)
    A[0], A[1] = 1, 1
    for i in range(2, N+1):
        A[i] = A[i-1] + A[i-2] * 2
    
    if N % 2 == 1:
        k = N // 2
        # 대칭의 수
        symmetry = A[k]
    else:
        k = N // 2
        if k == 0:
            symmetry = A[0]
        else:
            symmetry = A[k] + 2 * A[k-1]
    
    print((A[N] + symmetry) // 2)

main()