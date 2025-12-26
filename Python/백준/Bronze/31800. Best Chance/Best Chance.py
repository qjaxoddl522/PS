import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    profit = list(map(int, input().split()))
    price = list(map(int, input().split()))

    profitFirst, profitSecond = 0, 0
    for p in profit:
        if profitFirst <= p:
            profitSecond = profitFirst
            profitFirst = p
        elif profitSecond < p:
            profitSecond = p
    choicePrice = []
    for i in range(N):
        if profit[i] != profitFirst:
            choicePrice.append(profitFirst - price[i])
        else:
            choicePrice.append(profitSecond - price[i])
    
    pureProfit = []
    for i in range(N):
        pureProfit.append(profit[i] - choicePrice[i] - price[i])
    print(*pureProfit)

main()