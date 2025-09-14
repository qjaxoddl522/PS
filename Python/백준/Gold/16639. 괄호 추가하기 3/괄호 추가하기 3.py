import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    INF = float('inf')
    N = int(input())
    nums = []
    ops = []
    for s in input():
        if s == '+' or s == '-' or s == '*':
            ops.append(s)
        else:
            nums.append(int(s))
    
    n = len(nums)
    # dp[i][j] = i번째 부터 j번째 숫자까지 최소/최대 합
    dpmin = [[INF] * n for _ in range(n)]
    dpmax = [[-INF] * N for _ in range(n)]
    for i in range(n):
        dpmin[i][i] = dpmax[i][i] = nums[i]
    
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            curMin, curMax = INF, -INF
            for k in range(i, j):
                op = ops[k]
                leftMin, leftMax = dpmin[i][k], dpmax[i][k]
                rightMin, rightMax = dpmin[k+1][j], dpmax[k+1][j]
                if op == '+':
                    can = [leftMin + rightMin, leftMax + rightMax]
                elif op == '-':
                    can = [leftMax - rightMin, leftMin - rightMax]
                elif op == '*':
                    can = [leftMin * rightMin, leftMin * rightMax, leftMax * rightMin, leftMax * rightMax]
                curMin = min(curMin, *can)
                curMax = max(curMax, *can)
            dpmin[i][j] = curMin
            dpmax[i][j] = curMax
    print(dpmax[0][n-1])

main()