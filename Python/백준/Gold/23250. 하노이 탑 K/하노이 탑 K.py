import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    
    # 최저비트 자릿수
    d = (-K & K).bit_length()
    # N과 d의 홀짝이 같으면 반시계, 다르면 시계
    dir = 1 if (N + d) & 1 else -1
    # 원판 d가 K 이전까지 움직인 횟수
    m   = K >> d
    p   = (m * dir) % 3
    q   = (p + dir) % 3
    print(p+1, q+1)

main()