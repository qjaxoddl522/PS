import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    word = input()
    if N & 1 == 1:
        print("NO")
        return
    found = 0
    for i in range(len(word)):
        if i & 1 == 0:
            if word[i] == 'P' and found == 0:
                found += 1
            if word[i] == 'U' and found == 2:
                found += 1
        else:
            if word[i] == 'A' and found == 1:
                found += 1
            if word[i] == 'L' and found == 3:
                print("YES")
                break
    else:
        print("NO")

main()