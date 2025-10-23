import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def main():
    N = int(input())
    minn, maxx = int(1e9), -int(1e9)

    def backtrack(N, odd):
        nonlocal minn, maxx
        l = int(math.log10(N))+1
        # 홀수의 개수 구하기
        nn = N
        while nn > 0:
            odd += 1 if nn % 2 == 1 else 0
            nn //= 10
        
        # 정답 구하기
        if l == 1:
            minn = min(minn, odd)
            maxx = max(maxx, odd)
        
        # 수 나누기
        if l == 2:
            backtrack(N//10 + N%10, odd)
            return
        for i in range(1, l-1):
            for j in range(i+1, l):
                hap = 0
                nn = N
                # 오른쪽
                for k in range(l-j):
                    hap += (nn % 10) * (10 ** k)
                    nn //= 10
                # 가운데
                for k in range(j-i):
                    hap += (nn % 10) * (10 ** k)
                    nn //= 10
                # 왼쪽
                for k in range(i):
                    hap += (nn % 10) * (10 ** k)
                    nn //= 10
                backtrack(hap, odd)
    
    backtrack(N, 0)
    print(minn, maxx)

main()