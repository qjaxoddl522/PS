import sys
input = lambda: sys.stdin.readline().rstrip()

def Main():
    # 커버가능한 높이를 순서대로 스택
    height = [0]
    ans = 0
    for _ in range(int(input())):
        x, y = map(int, input().split())
        # 현재가 높을 경우 커버 가능한 높이에 추가
        if height[-1] < y:
            height.append(y)
            ans += 1
        # 현재가 낮을 경우 현재 높이까지 pop
        else:
            while height[-1] > y:
                height.pop()
            if height[-1] != y:
                height.append(y)
                ans += 1
    print(ans)

Main()