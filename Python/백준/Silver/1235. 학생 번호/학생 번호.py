import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    nums = [input() for _ in range(N)]
    L = len(nums[0])
    for i in range(L-1, -1, -1):
        same = set()
        for j in range(N):
            code = nums[j][i:]
            if code in same:
                break
            same.add(code)
        else:
            print(L-i)
            break

main()