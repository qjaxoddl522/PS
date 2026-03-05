import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    for _ in range(int(input())):
        inp = list(map(int, input().split()))
        soilder = dict()
        most = -1
        for i in range(1, len(inp)):
            num = inp[i]
            if num not in soilder:
                soilder[num] = 0
            soilder[num] += 1
            if most == -1 or soilder[most] < soilder[num]:
                most = num
        if soilder[most] > inp[0] // 2:
            print(most)
        else:
            print("SYJKGW")
    
main()