import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def main():
    # daldidalgo = 8초, daldidan = 2초
    N = int(input())
    print(10 + math.floor(math.log2(N)))

main()