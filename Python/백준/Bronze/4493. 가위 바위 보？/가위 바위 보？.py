import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    rsp = ['R', 'S', 'P']
    for _ in range(int(input())):
        p1w = 0
        for _ in range(int(input())):
            p1, p2 = input().split()
            p1, p2 = rsp.index(p1), rsp.index(p2)
            if p2 - p1 == 1 or p2 + 2 == p1:
                p1w += 1
            elif p1 - p2 == 1 or p1 + 2 == p2:
                p1w -= 1
        if p1w > 0:
            print("Player 1")
        elif p1w < 0:
            print("Player 2")
        else:
            print("TIE")

main()