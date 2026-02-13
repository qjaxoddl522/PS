import sys
input = lambda: sys.stdin.readline().rstrip()

"""
유클리드 호제법을 이용 => O(N)
"""
def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    def ACD(A, B):
        if B > 0:
            return ACD(B, A%B)
        return A

    ans = []
    for a in A:
        if ACD(a, X) == 1:
            ans.append(a)
    print(sum(ans)/len(ans))
    
main()