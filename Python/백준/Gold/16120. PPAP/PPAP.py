import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input()
    n = len(s)
    i = 0
    pCnt = 0

    while i < n:
        if s[i] == 'P':
            pCnt += 1
            i += 1
        else:
            # 직전에 P가 2개 이상 있었고, 바로 다음 문자가 P여야 PPAP
            if pCnt >= 2 and i + 1 < n and s[i + 1] == 'P':
                pCnt -= 1
                i += 2
            else:
                print("NP")
                return

    print("PPAP" if pCnt == 1 else "NP")

main()