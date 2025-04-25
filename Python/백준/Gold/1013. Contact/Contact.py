import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        S = input()
        idx = 0
        flag = True
        while idx < len(S) and flag:
            if S[idx] == '0':
                if idx+1 < len(S) and S[idx+1] == '1':
                    idx += 2
                else:
                    flag = False
                    break
            else:
                if idx+2 < len(S) and S[idx+1] == '0' and S[idx+2] == '0':
                    idx += 2
                    while idx < len(S) and S[idx] == '0':
                        idx += 1
                    if idx < len(S) and S[idx] == '1':
                        oneAmount = 0
                        while idx < len(S) and S[idx] == '1':
                            idx += 1
                            oneAmount += 1
                        # 1다음에 0이 한 개 나오면 01로 판단
                        # 이전에 1이 두 개, 0이 두 개 이상 나오면 새로운 100+1+로 판단
                        if idx+1 < len(S) and oneAmount >= 2 and S[idx] == '0' and S[idx+1] == '0':
                            idx -= 1
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
        
        print("YES" if flag else "NO")
            
main()
