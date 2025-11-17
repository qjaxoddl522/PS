import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    for _ in range(N):
        word = sorted(input())
        overlap = set()
        ans = []
        used = bytearray(len(word))

        def backtrack(now):
            if len(now) == len(word):
                if now not in overlap:
                    ans.append(now)
                    overlap.add(now)
                return
            for i in range(len(word)):
                if used[i]:
                    continue
                if i > 0 and word[i] == word[i-1] and not used[i-1]:
                    continue
                used[i] = True
                backtrack(now + word[i])
                used[i] = False
        backtrack("")
        print(*ans, sep='\n')
    
main()