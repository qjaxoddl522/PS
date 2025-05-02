import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, M, K = map(int, input().split())

    # 4가지 경우의 칸에 곰팡이가 있어야 함
    # [합짝수/X짝수, 합짝수/X홀수, 합홀수/X짝수, 합홀수/X홀수]
    conditions = [False] * 4

    for _ in range(K):
        x, y = map(int, input().split())
        if (x + y) % 2 == 0:
            if x % 2 == 0:
                conditions[0] = True
            else:
                conditions[1] = True
        else:
            if x % 2 == 0:
                conditions[2] = True
            else:
                conditions[3] = True
    
    print("YES" if all(conditions) else "NO")

main()