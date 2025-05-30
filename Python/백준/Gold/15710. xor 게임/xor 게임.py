import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b, n = map(int, input().split())
    print(pow(pow(2, 31, 1000000007), n-1, 1000000007))

main()