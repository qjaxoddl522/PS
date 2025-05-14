import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        trees = []
        for _ in range(N):
            trees.append(list(map(int, input().split())))
        trees.sort()
        
        unit = []
        firstx = trees[0][0]
        for i in range(N):
            if firstx == trees[i][0]:
                unit.append(trees[i][1])
            elif trees[i][1] != unit[i % len(unit)]:
                print("NOT BALANCED")
                break
        else:
            print("BALANCED")

main()