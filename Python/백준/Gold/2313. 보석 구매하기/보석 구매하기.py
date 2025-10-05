import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    def max_subarray(ls):
        cur = best = ls[0]
        bestLen = 0
        start = L = R = 0
        for i in range(1, len(ls)):
            # 새로 시작하는게 이득이면 기존 합 손절
            if ls[i] >= cur + ls[i]:
                cur = ls[i]
                start = i
            else:
                cur += ls[i]
            
            if (cur == best and bestLen > i - start) or cur > best:
                best = cur
                bestLen = i - start
                L, R = start, i
        return best, L, R
    
    summ = 0
    result = []
    for _ in range(int(input())):
        input()
        b, l, r = max_subarray(list(map(int, input().split())))
        summ += b
        result.append((l+1, r+1))
    print(summ)
    for r in result:
        print(*r)

main()
