import sys
input = lambda: sys.stdin.readline().rstrip()

"""
최악의 경우 최대 비용으로 스패닝 트리 만들기
최선의 경우 최소 비용으로 스패닝 트리 만들기
"""
def main():
    N, M = map(int, input().split())
    # 오르막길, 내리막길
    upline, downline = [], []
    for _ in range(M+1):
        A, B, C = map(int, input().split())
        if C == 0:
            upline.append((A, B))
        else:
            downline.append((A, B))

    def union(a, b):
        pa, pb = find(a), find(b)
        parent[pa] = pb

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]
    
    # 최악의 경우 구하기
    parent = [i for i in range(N+1)]
    worstCost = 0
    for a, b in upline:
        if find(a) != find(b):
            union(a, b)
            worstCost += 1

    # 최선의 경우 구하기
    parent = [i for i in range(N+1)]
    bestCost = 0
    for a, b in downline:
        if find(a) != find(b):
            union(a, b)
    for a, b, in upline:
        if find(a) != find(b):
            union(a, b)
            bestCost += 1
    print(worstCost ** 2 - bestCost ** 2)

main()