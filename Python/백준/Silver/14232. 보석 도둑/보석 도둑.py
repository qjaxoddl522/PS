import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    factors = []
    
    while N % 2 == 0:
        factors.append(2)
        N //= 2
        
    d = 3
    while d * d <= N:
        if N % d == 0:
            factors.append(d)
            N //= d
        else:
            d += 2 
    
    if N > 1:
        factors.append(N)
        
    print(len(factors))
    print(*factors)
    
main()