import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    num = list(map(int, list(input())))
    
    stack = []
    removed = 0
    for digit in num:
        # 스택 최상단보다 크면 삭제
        while removed < K and stack and stack[-1] < digit:
            stack.pop()
            removed += 1
        stack.append(digit)
    
    # 잉여 제거량은 뒤에서부터 제거
    answer = stack[:len(stack) - K + removed]
    print(*answer, sep='')

main()