import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    attack = [list(map(int, input().split())) for _ in range(N)]

    for k in range(N):
        possible = True
        minn = -float('inf')
        maxx = float('inf')

        for i in range(N):
            if i > 0:
                minn -= 1
                maxx += 1
            
            if i != k:
                minn = max(minn, attack[i][0])
                maxx = min(maxx, attack[i][1])
            
            if minn > maxx:
                possible = False
                break
        
        if possible:
            print("World Champion")
            return

    print("Surrender")

main()