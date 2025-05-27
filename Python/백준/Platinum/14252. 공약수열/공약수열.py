import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    seq = sorted(map(int, input().split()))
    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    ans = 0
    for i in range(1, N):
        g = gcd(seq[i], seq[i-1])
        if g > 1:
            # 한 개 추가
            for mid in range(seq[i-1] + 1, seq[i]):
                if gcd(mid, seq[i-1]) == 1 and gcd(seq[i], mid) == 1:
                    ans += 1
                    break
            # 불가능할 경우 두 개 추가
            else:
                ans += 2
    print(ans)

main()