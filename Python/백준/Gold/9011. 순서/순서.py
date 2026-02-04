import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        N = int(input())
        R = list(map(int, input().split()))

        for i in range(N):
            if R[i] > i:
                print("IMPOSSIBLE")
                break
        else:
            S = [0] * N
            candidates = [i for i in range(1, N + 1)]
            
            for i in range(N-1, -1, -1):
                S[i] = candidates.pop(R[i])
                
            print(*S)
    
main()