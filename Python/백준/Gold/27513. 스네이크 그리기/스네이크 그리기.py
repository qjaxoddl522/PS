import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    if n & 1 == 1 and m & 1 == 1:
        print(n*m-1)
        for i in range(1, n+1):
            print(i, 1)
        for i in range(2, m):
            if i & 1 == 0:
                print(n, i)
                print(n-1, i)
            else:
                print(n-1, i)
                print(n, i)
        print(n-1, m)
        for i in range(n-2, 0, -1):
            if i & 1 == 0:
                for j in range(2, m+1):
                    print(i, j)
            else:
                for j in range(m, 1, -1):
                    print(i, j)
    
    elif n & 1 == 0:
        print(n*m)
        for i in range(1, n+1):
            print(i, 1)
        for i in range(n, 0, -1):
            if i & 1 == 0:
                for j in range(2, m+1):
                    print(i, j)
            else:
                for j in range(m, 1, -1):
                    print(i, j)

    elif m & 1 == 0:
        print(n*m)
        for j in range(1, m+1):
            print(1, j)
        for j in range(m, 0, -1):
            if j & 1 == 0:
                for i in range(2, n+1):
                    print(i, j)
            else:
                for i in range(n, 1, -1):
                    print(i, j)

main()