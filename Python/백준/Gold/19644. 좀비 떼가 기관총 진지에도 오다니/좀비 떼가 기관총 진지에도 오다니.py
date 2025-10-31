import sys
input = lambda: sys.stdin.readline().rstrip()

"""
처음을 제외하면 지뢰를 쓰지 않는 한 들어가는 데미지는 일정
일일이 데미지를 매 턴 계산할 필요 없이 바로 앞에 있는 좀비에게만 그동안 누적 가능한 데미지를 주면 됨
만약 누적 가능한 데미지로 죽일 수 없을 경우 지뢰를 사용하고 누적 데미지를 줄임
지뢰까지 전부 사용한 상태에서 죽일 수 없을 경우 살아남을 수 없음
"""
def Main():
    L = int(input())
    RR, RD = map(int, input().split())
    C = int(input())
    zombie = [int(input()) for _ in range(L)]

    # 인덱스에 추가된 시간이 되면 데미지가 증가
    damagePlus = [i for i in range(RR)]
    damageIdx = 0

    damage = 0
    for time in range(L):
        if damageIdx < len(damagePlus) and damagePlus[damageIdx] == time:
            damage += RD
            damageIdx += 1
        
        # 누적 데미지로 죽일 수 없음
        if zombie[time] > damage:
            # 지뢰가 있음
            if C > 0:
                damage -= RD
                damagePlus.append(time + RR)
                C -= 1
            # 지뢰가 없으면 생존불가
            else:
                print("NO")
                break
    else:
        print("YES")

Main()