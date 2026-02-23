import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    F = int(input())

    for n in range(100):
        NN = N // 100 * 100 + n
        if NN % F == 0:
            print(f"{n:02}")
            break

main()