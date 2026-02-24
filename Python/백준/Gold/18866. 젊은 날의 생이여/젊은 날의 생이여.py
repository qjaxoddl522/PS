import sys
input = lambda: sys.stdin.readline().rstrip()

"""
방향 별로 한바퀴 순회하며 최대 행복도, 최소 피로도를 누적으로 기록
누락된 값은 현재 최대 행복도, 현재 최소 피로도로 기록
이후 뒤에서부터 순회하여 조건을 충족하는지 확인
"""
def main():
    N = int(input())
    info = [tuple(map(int, input().split())) for _ in range(N)]

    uMinUp, uMaxDown = [0] * N, [0] * N
    vMaxUp, vMinDown = [0] * N, [0] * N
    uMinUp[0], uMaxDown[-1] = info[0][0] if info[0][0] > 0 else float('inf'), info[-1][0]
    vMaxUp[0], vMinDown[-1] = info[0][1], info[-1][1] if info[-1][1] > 0 else float('inf')

    for i in range(1, N):
        du, dv = info[i]
        uu, uv = info[-i-1]
        uMinUp[i] = min(uMinUp[i-1], du if du > 0 else uMinUp[i-1])
        uMaxDown[-i-1] = max(uMaxDown[-i], uu if uu > 0 else uMaxDown[-i])
        vMaxUp[i] = max(vMaxUp[i-1], dv if dv > 0 else vMaxUp[i-1])
        vMinDown[-i-1] = min(vMinDown[-i], uv if uv > 0 else vMinDown[-i])
    
    for i in range(N-2, -1, -1):
        if uMinUp[i] > uMaxDown[i+1] and vMaxUp[i] < vMinDown[i+1]:
            print(i+1)
            break
    else:
        print(-1)

main()