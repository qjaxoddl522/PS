import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = list(map(int, input().split()))

    AMAX = 1000000
    isPrime = [True] * (AMAX+1)
    for i in range(2, int(AMAX ** 0.5)+1):
        if isPrime[i]:
            for j in range(i * i, AMAX + 1, i):
                isPrime[j] = False
    
    isUp = True
    for i in range(N):
        # 내림차순 확인
        if i > 0 and A[i-1] > A[i]:
            isUp = False

        # 합성수이거나, 연속된 두 수 모두 1이 아니라면 무제한 교환 가능하므로 비내림차순을 만들 수 있다
        if not isPrime[A[i]] or (A[i] != 1 and (i > 0 and A[i-1] != 1)):
            print("YES")
            break
    else:
        print("YES" if isUp else "NO")    

main()