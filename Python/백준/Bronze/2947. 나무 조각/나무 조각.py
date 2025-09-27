import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    X = list(map(int, input().split()))
    for i in range(4, -1, -1):
        for j in range(i):
            if X[j] > X[j+1]:
                X[j], X[j+1] = X[j+1], X[j]
                print(*X)

main()