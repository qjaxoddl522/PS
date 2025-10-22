import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def hanoi(n, start, mid, end):
        if n == 1:
            print(start, end)
            return
        hanoi(n-1, start, end, mid)
        print(start, end)
        hanoi(n-1, mid, start, end)

    N = int(input())
    print(pow(2, N)-1)
    if N <= 20:
        hanoi(N, 1, 2, 3)

main()