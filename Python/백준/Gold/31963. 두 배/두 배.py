import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    answer = 0
    cnt = [0] * N
    for i in range(1, N):
        ratio = math.ceil(math.log2(A[i-1] / A[i])) + cnt[i-1]
        if ratio > 0:
            cnt[i] = ratio
            answer += cnt[i]
    print(answer)

main()
