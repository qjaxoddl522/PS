import sys
input = lambda: sys.stdin.readline().rstrip()
from decimal import Decimal, getcontext

def main():
    A, B = input().split()
    B = int(B)
    digits = len(A.replace('.', ''))
    getcontext().prec = digits * B + 10 

    result = Decimal(A) ** B
    print(format(result, 'f'))

main()