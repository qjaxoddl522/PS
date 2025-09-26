import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    X = list(map(int, input().split()))

    # 밑장빼기를 내 차례에 했을 때 얻는 점수
    rightMe = sum([x for x in X[1::2]])
    # 밑장빼기를 상대 차례에 했을 때 얻는 점수
    rightOp = rightMe - X[-1]
    # 밑장빼기를 안했을 때 얻는 점수
    left = 0
    ans = rightMe
    for i in range(0, N, 2):
        left += X[i]
        rightMe -= X[i+1]
        ans = max(ans, left + rightMe, left + rightOp)
        rightOp -= X[i+1]
    print(ans)

main()