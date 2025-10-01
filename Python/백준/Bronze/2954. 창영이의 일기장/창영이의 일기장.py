import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    moeum = {'a', 'e', 'i', 'o', 'u'}
    ans = []

    S = input()
    i = 0
    while i < len(S):
        ans += S[i]
        if S[i] in moeum and (i+2 < len(S) and S[i+1] == 'p' and S[i+2] in moeum):
            i += 2
        i += 1
    print(*ans, sep='')

main()