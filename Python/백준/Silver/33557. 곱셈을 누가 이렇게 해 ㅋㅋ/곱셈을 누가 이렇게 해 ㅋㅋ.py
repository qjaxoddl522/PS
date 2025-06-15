import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        A, B = map(int, input().split())
        originResult = str(A * B)
        calc = []
        while A > 0 or B > 0:
            a = A % 10 if A > 0 else 1
            b = B % 10 if B > 0 else 1
            
            calc.append(a * b)
            A //= 10
            B //= 10
        
        result = ""
        for i in range(len(calc)-1, -1, -1):
            result += str(calc[i])
        print(1 if result == originResult else 0)
        #print(result, originResult)

main()