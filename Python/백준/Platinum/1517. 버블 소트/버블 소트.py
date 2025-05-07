import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    # 병합정렬을 수행하며 횟수 계산
    def recursion(ls):
        nonlocal ans
        if len(ls) == 1:
            return ls
        
        mid = len(ls) // 2
        leftLs = recursion(ls[:mid])
        rightLs = recursion(ls[mid:])

        i, j = 0, 0
        newLs = []
        while i < len(leftLs) and j < len(rightLs):
            if leftLs[i] > rightLs[j]:
                ans += len(leftLs) - i
                newLs.append(rightLs[j])
                j += 1
            else:
                newLs.append(leftLs[i])
                i += 1
        newLs.extend(leftLs[i:])
        newLs.extend(rightLs[j:])
        return newLs

    N = int(input())
    ls = list(map(int, input().split()))
    ans = 0
    recursion(ls)
    print(ans)

main()