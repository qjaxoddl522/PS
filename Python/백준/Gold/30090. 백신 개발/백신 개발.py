import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    words = [input() for _ in range(N)]

    ans = 100
    used = bytearray(N)
    # 합친 단어 수, 단어
    def dfs(num, word):
        nonlocal ans
        for i in range(N):
            if not used[i]:
                newWord = combine(word, words[i])
                if len(newWord) >= ans:
                    continue
                if num == N-1:
                    ans = min(ans, len(newWord))
                used[i] = True
                dfs(num + 1, newWord)
                used[i] = False
    
    def combine(w1:str, w2:str):
        for i in range(max(0, len(w1)-len(w2)), len(w1)):
            for j in range(len(w1)-i):
                if w1[i+j] != w2[j]:
                    break
            else:
                return w1 + w2[j+1:]
        return w1 + w2

    dfs(0, "")
    print(ans)

main()