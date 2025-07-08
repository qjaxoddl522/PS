import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    satis = [list(map(int, input().split())) for _ in range(N)]

    # i번 고양이가 j번 리본을 골랐을 때의 최대 만족도 합
    prev = satis[0][:]
    for i in range(1, N):
        leftmax = [0] * K
        leftmax[0] = prev[0]
        for j in range(1, K):
            leftmax[j] = max(leftmax[j-1], prev[j])

        rightmax = [0] * K
        rightmax[-1] = prev[-1]
        for j in range(K-2, -1, -1):
            rightmax[j] = max(rightmax[j+1], prev[j])
        
        cur = [0] * K
        for j in range(K):
            left = leftmax[j-1] if j > 0 else 0
            right = rightmax[j+1] if j < K-1 else 0
            cur[j] = max(left, right) + satis[i][j]
        
        prev = cur
    print(max(prev))

main()