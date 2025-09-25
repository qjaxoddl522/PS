import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    books = list(map(int, input().split()))

    order = [[], []]
    for b in books:
        if b > 0:
            order[0].append(b)
        else:
            order[1].append(-b)
    order[0].sort()
    order[1].sort()
    
    if not order[1]:
        last = 0
    elif not order[0]:
        last = 1
    elif order[0][-1] > order[1][-1]:
        last = 0
    else:
        last = 1
    
    ans = 0
    for o in range(2):
        if order[o] and last == o:
            ans -= order[o][-1]
        while order[o]:
            ans += order[o][-1] * 2
            for _ in range(K):
                if not order[o]:
                    break
                order[o].pop()
    print(ans)

main()