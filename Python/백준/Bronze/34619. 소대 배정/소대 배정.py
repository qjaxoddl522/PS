import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b, n, k = map(int, input().split())
    order = k // n if k % n == 0 else k // n + 1
    print(order//b+1 if order%b>0 else order//b, order%b if order%b>0 else b)

main()