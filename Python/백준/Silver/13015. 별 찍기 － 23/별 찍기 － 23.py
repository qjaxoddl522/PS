import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    
    print("*"*N + " "*((N-1)*2-1) + "*"*N)
    for i in range(1, N-1):
        print(" "*i + "*" + " "*(N-2) + "*" + " "*((N-i-1)*2-1) + "*" + " "*(N-2) + "*")
    print(" "*(N-1) + "*" + " "*(N-2) + "*" + " "*(N-2) + "*")
    for i in range(N-2, 0, -1):
        print(" "*i + "*" + " "*(N-2) + "*" + " "*((N-i-1)*2-1) + "*" + " "*(N-2) + "*")
    print("*"*N + " "*((N-1)*2-1) + "*"*N)

main()