import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    ls = [int(input()) for _ in range(N)]

    ans = 0
    stack = []
    for t in ls:
        # 현재 높이보다 작은 높이를 지우면서 연속 개수 더하기
        while stack and stack[-1][0] < t:
            ans += stack[-1][1]
            stack.pop()

        cnt = 1
        if stack:
            # 스택 최상단 높이가 같으면 연속 수 만큼 더하기
            if stack[-1][0] == t:
                ans += stack[-1][1]
                cnt = stack[-1][1] + 1
                stack.pop()

                # 뒤에 더 높은 사람이 있을 경우 쌍 추가
                if stack:
                    ans += 1
            else:
                ans += 1
        stack.append((t, cnt))
    
    print(ans)

main()