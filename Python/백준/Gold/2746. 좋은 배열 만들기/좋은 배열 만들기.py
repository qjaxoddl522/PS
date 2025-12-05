import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left, bisect_right

def main():
    N = int(input())
    A = list(sorted(map(int, input().split())))
    
    totalSum = sum(A)
    ans = 0
    
    # 원래 최댓값 A[N-1]이 살아남는 경우
    targetSum = totalSum - 2 * A[N-1]
    temp = A[:N-1]
    for i in range(len(temp)):
        needed = targetSum - temp[i]
        ans += (bisect_right(temp, needed, lo=i+1) - bisect_left(temp, needed, lo=i+1))

    # A[N-1]은 제거되고, A[N-2]가 최댓값이 되는 경우
    if N >= 3:
        neededX = totalSum - A[N-1] - 2 * A[N-2]
        temp = A[:N-2]
        ans += (bisect_right(temp, neededX) - bisect_left(temp, neededX))

    # A[N-1], A[N-2] 둘 다 제거되는 경우
    if N >= 3:
        if totalSum - A[N-1] - A[N-2] == 2 * A[N-3]:
            ans += 1

    print(ans)

main()