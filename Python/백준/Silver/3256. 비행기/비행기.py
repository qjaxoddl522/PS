import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    R = [int(input()) for _ in range(N)]
    M = max(R)

    time = 0
    # 0: 비어있는 상태  양수: 이동하는 중  음수: 짐을 넣는 중
    airplane = [0] * (M+1)
    RIdx = 0
    while True:
        isAllSeated = True
        for i in range(M, 0, -1):
            if airplane[i] > 0:
                isAllSeated = False
                if i+1 <= M and airplane[i+1] == 0:
                    airplane[i+1] = airplane[i]-1
                    if airplane[i+1] == 0:
                        airplane[i+1] = -5
                    airplane[i] = 0
            elif airplane[i] < 0:
                airplane[i] += 1
                if airplane[i] != 0:
                    isAllSeated = False

        if RIdx < N and airplane[1] == 0:
            airplane[1] = R[RIdx]-1 if R[RIdx] > 1 else -5
            RIdx += 1
            isAllSeated = False
        
        if isAllSeated:
            break
        time += 1
    print(time)
    
main()