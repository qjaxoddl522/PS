import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def main():
    N, M = map(int, input().split())
    bus = [tuple(map(int, input().split())) for _ in range(M)]

    busIdx = 0
    # 정류장에 들어가지 못한 대기 버스
    wait = deque()
    # 정류장 대기 남은 시간 -1: 비어있음
    stop = [-1] * (N+1)

    time = 0
    while wait or busIdx < M:
        # 새로운 버스가 정차할 수 있는 정류장 번호
        stopNum = 1
        # 시간의 흐름, 버스 이동
        time += 1
        for i in range(1, N+1):
            if stop[i] > 0:
                stop[i] -= 1
            # 정차 중인 버스 출발
            if stop[i] == 0 and stop[i-1] < 0:
                stop[i] = -1
            elif stop[i] >= 0:
                stopNum = i+1

        # 새로운 버스가 들어올 시간이 됨
        while busIdx < M and bus[busIdx][0] == time:
            wait.append(bus[busIdx][1])
            busIdx += 1

        # 큐에 있던 버스가 들어올 수 있는지 확인
        while wait and stopNum <= N:
            stop[stopNum] = wait.popleft()
            if not wait and busIdx == M:
                print(stopNum)
                return
            stopNum += 1

main()