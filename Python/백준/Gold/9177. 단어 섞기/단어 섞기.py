import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    for n in range(1, N+1):
        A, B, C = input().split()
        lenA, lenB, lenC = len(A), len(B), len(C)

        # 길이 안 맞으면 바로 불가능
        possible = False
        if lenA + lenB == lenC:
            # dp[i][j] = A에서 i개, B에서 j개 사용해서 C의 앞 i+j 글자를 만들 수 있는가
            dp = [[False] * (lenB + 1) for _ in range(lenA + 1)]
            dp[0][0] = True

            for i in range(lenA + 1):
                for j in range(lenB + 1):
                    if i == 0 and j == 0:
                        continue
                    # C의 현재 인덱스
                    k = i + j - 1

                    ok = False
                    if i > 0 and dp[i-1][j] and A[i-1] == C[k]:
                        ok = True
                    if j > 0 and dp[i][j-1] and B[j-1] == C[k]:
                        ok = True

                    dp[i][j] = ok

            possible = dp[lenA][lenB]

        print(f"Data set {n}: {'yes' if possible else 'no'}")

main()