import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    MOD = 10 ** 9 + 7
    H, x = map(int, input().split())
    snow = [int(input()) for _ in range(H)]

    hap = 0
    for i in range(H-1, -1, -1):
        hap = (hap + snow[i]) * x % MOD
    print(hap)
    
main()