import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())

    def isPrime(num):
        if num < 2: return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if N == 1:
        print(-1)
    else:
        result = []
        while True:
            found = False
            limit = int(N**0.5)
            
            for i in range(2, limit + 1):
                if N % i == 0:
                    if isPrime(i): 
                        continue
                    
                    quotient = N // i
                    # 남은 수가 소수면 안됨
                    if quotient != 1 and isPrime(quotient):
                        continue
                    
                    result.append(i)
                    N = quotient
                    found = True
                    break
            
            # 더 이상 나누어 떨어지는 합성수가 없음
            if not found:
                if N > 1:
                    # 남은게 소수면 실패
                    if isPrime(N):
                        result = [-1]
                    else:
                        result.append(N)
                break
                
        print(*result)

main()