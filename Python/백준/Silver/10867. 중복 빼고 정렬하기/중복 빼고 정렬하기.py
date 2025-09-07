import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    print(*sorted(list(set(map(int, input().split())))))

main()