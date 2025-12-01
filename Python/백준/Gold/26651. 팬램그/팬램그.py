import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    X = int(input())

    if X == 0:
        print("GBSISTHEBEST")
        return

    a = int(X**0.5)
    z = X // a
    remain = X % a
    
    middle = "".join(chr(c) for c in range(66, 90))
    part1 = ("A" * a) + middle + ("Z" * z)
    
    part2 = ""
    if remain > 0:
        part2 = "A" + middle + ("Z" * remain)
    
    print(part1 + part2)

main()