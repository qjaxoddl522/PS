import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def abc(a, b):
        if b <= 0:
            return a
        return abc(b, a%b)
    
    a, b, L = map(int, input().split())
    lcm = a * b // abc(a, b)
    if L % lcm != 0:
        print(-1)
    else:
        c = 1
        d = 2
        while d * d <= L:
            if L % d == 0:
                power = 1
                while L % d == 0:
                    power *= d
                    L //= d
                
                # A가 해당 소인수 power를 온전히 포함하지 못하면 c가 그 역할을 대신해야 함
                if lcm % power != 0:
                    c *= power
            d += 1
            
        if L > 1:
            if lcm % L != 0:
                c *= L
                
        print(c)

main()