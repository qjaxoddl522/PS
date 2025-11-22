import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        l, r = map(int, input().split())

        if r >= 4:
            print(r)
        else:
            s = "".join(str(pow(2, n)) for n in range(l, r + 1))
            z = int(s)
            
            if z == 0:
                print(0)
            else:
                print((z & -z).bit_length() - 1)

main()