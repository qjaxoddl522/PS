import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        A, B = map(int, input().split())
        print("yes")

main()