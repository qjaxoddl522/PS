import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(N):
        if i+1 == nums[i]:
            print(-1)
            return
    print(1000003)
    
main()