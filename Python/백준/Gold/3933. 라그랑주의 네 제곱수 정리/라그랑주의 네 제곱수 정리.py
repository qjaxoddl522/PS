import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    MAX = pow(2, 15)
    dp = [[0] * (MAX + 1) for _ in range(5)]
    dp[0][0] = 1

    m = int(MAX**0.5)
    for i in range(1, m + 1):
        sq = i * i
        
        for cnt in range(1, 5):
            for val in range(sq, MAX + 1):
                dp[cnt][val] += dp[cnt-1][val-sq]

    while True:
        n = int(input())
        if n == 0: break
        print(sum(dp[k][n] for k in range(1, 5)))

main()