import sys
input = lambda: sys.stdin.readline().rstrip()

"""
두 점을 골라서 사각형을 만들수 있는지 확인 => O(N^2)
"""
def main():
    N = int(input())
    pointList = [tuple(map(int, input().split())) for _ in range(N)]
    pointSet = set(pointList)

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            p1, p2 = pointList[i], pointList[j]
            # 모두 좌표가 달라야 함
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue
            
            # 나머지 두 점이 존재하면 카운팅
            if (p1[0], p2[1]) in pointSet and (p2[0], p1[1]) in pointSet:
                count += 1
    # 2개씩 중복 계산되므로 나누기
    print(count // 2)
    
main()