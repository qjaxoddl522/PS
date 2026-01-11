import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    words = [input() for _ in range(N)]
    ans = []
    for i in range(len(words[0])):
        isSame = True
        for j in range(N-1):
            if words[j][i] != words[j+1][i]:
                isSame = False
                break
        ans.append(words[0][i] if isSame else "?")
    print(''.join(ans))

main()