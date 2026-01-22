import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    L, T = map(int, input().split())
    T = T % (L * 2)
    N = int(input())
    ants = []
    for _ in range(N):
        l, d = input().split()
        l = int(l) if d == 'D' else L - int(l)
        if l + T >= L * 2 or l + T < L:
            loc = (l + T) % L
        else:
            loc = L - ((l + T) % L)
        ants.append(loc if d == 'D' else L - loc)
    print(*sorted(ants))
    
main()