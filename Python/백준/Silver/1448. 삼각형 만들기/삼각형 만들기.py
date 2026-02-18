import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
긴 순서대로 정렬해서 긴 세 변이 삼각형이 되는지 확인 => 안되면 가장 긴 변을 없애고 다음으로 긴거 배치
"""
def main():
    N = int(input())
    lines = sorted([int(input()) for _ in range(N)])
    
    i = N-4
    q = deque([lines[-1], lines[-2], lines[-3]])
    while True:
        if q[0] < q[1] + q[2]:
            print(sum(q))
            break
        if i < 0:
            print(-1)
            break
        q.popleft()
        q.append(lines[i])
        i -= 1

main()