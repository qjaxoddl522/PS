import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left

def main():
    N = int(input())
    price = list(map(int, input().split()))
    value = list(map(int, input().split()))
    K = int(input())
    input()
    # 가지고 있는 스티커 다 팔고 시작
    ownMoney = sum([price[i] for i in map(int, input().split())])

    # minPrice[가치합] = 가격 합 중 최솟값
    minPriceLeft = dict()
    minPriceRight = dict()
    def writeMinPrice(idx, end, valueSum, priceSum, minPrice):
        if idx == end:
            if valueSum in minPrice:
                minPrice[valueSum] = min(minPrice[valueSum], priceSum)
            else:
                minPrice[valueSum] = priceSum
            return
        writeMinPrice(idx+1, end, valueSum, priceSum, minPrice)
        writeMinPrice(idx+1, end, valueSum + value[idx], priceSum + price[idx], minPrice)
    writeMinPrice(0, N//2, 0, 0, minPriceLeft)
    writeMinPrice(N//2, N, 0, 0, minPriceRight)

    # 필요한 돈
    need = int(1e9)
    valueRight = list(sorted(minPriceRight.keys()))
    costRight = [minPriceRight[v] for v in valueRight]

    # sufMin[가치합] = 가치합 이상에서의 최소 비용
    sufMin = [0] * len(valueRight)
    sufMin[-1] = costRight[-1]
    for i in range(len(valueRight) - 2, -1, -1):
        sufMin[i] = min(costRight[i], sufMin[i + 1])

    for v, p in minPriceLeft.items():
        idx = bisect_left(valueRight, K - v)
        if idx < len(valueRight):
            need = min(need, p + sufMin[idx])
    # 원래 가지고 있던 돈만큼 빼기
    print(max(0, need - ownMoney) if need < int(1e9) else -1)

main()