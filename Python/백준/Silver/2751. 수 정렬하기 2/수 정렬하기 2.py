import sys

arr = []
for _ in range(int(sys.stdin.readline())):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in arr:
    print(i)