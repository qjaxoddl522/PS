import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    comp = input()
    stack = []
    curLen = 0  # 현재 괄호 깊이에서의 길이

    for i in range(len(comp)):
        s = comp[i]
        if s == '(':
            mult = int(comp[i-1])
            curLen -= 1 
            
            # 안쪽 길이를 세기 위해 cur_len 초기화
            stack.append((curLen, mult))
            curLen = 0
        elif s == ')':
            # 괄호가 닫히면 스택에서 꺼내기
            prevLen, mult = stack.pop()
            curLen = prevLen + (curLen * mult)
        else:
            # 다음이 (면 다시 1 빼기
            curLen += 1

    print(curLen)

main()