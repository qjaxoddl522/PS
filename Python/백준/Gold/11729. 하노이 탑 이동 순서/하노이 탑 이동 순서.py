def hanoi(n, st, to, via):
    if n==1:
        print(st, to)
    else:
        hanoi(n-1, st, via, to)
        print(st, to)
        hanoi(n-1, via, to, st)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)