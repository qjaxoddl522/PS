import sys

n = int(input())
tree = [[] for _ in range(n)]
p = list(map(int,sys.stdin.readline().split()))
for i in range(n):
    tree[i] = p[i]
remove = int(input())

def delete(remove):
    tree[remove] = -2
    for i in range(n):
        if tree[i] == remove:
            tree[i] = -2
            delete(i)
delete(remove)
cnt = 0
for i in range(n):
    if tree[i] != -2:
        err = 0
        for j in tree:
            if j == i:
                err = 1
                break
        if err == 0:
            cnt += 1
print(cnt)