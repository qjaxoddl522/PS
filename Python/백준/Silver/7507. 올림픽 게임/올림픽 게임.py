import sys
input = lambda: sys.stdin.readline().rstrip()

"""
날짜별로 구분 후 종료 시간 순서대로 정렬
종료 시간과 다음 시작 시간을 비교하며 시작 가능한지 확인
"""
def main():
    for scenario in range(1, int(input())+1):
        if scenario > 1: print()
        # 날짜별로 정리된 경기들
        match = dict()
        for _ in range(int(input())):
            d, s, e = map(int, input().split())
            if d not in match:
                match[d] = []
            match[d].append((s, e))
        
        # 시청한 경기 수
        watched = 0
        for mat in match.keys():
            match[mat].sort(key = lambda x: x[1])
            endTimeLast = -1
            for s, e in match[mat]:
                if endTimeLast <= s:
                    endTimeLast = e
                    watched += 1
        print(f"Scenario #{scenario}:")
        print(watched)
    
main()