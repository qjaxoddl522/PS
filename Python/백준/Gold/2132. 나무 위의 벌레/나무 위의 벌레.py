import sys
sys.setrecursionlimit(int(1e9))
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    fruit = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)
    
    # [최대 과일 수, 시작 노드]
    ans = [0, 1]
    # 현재 노드에서 가져올 수 있는 가장 많은 열매 반환
    def dfs(parent, now):
        nonlocal ans
        # 리프노드 확인
        if parent and len(graph[now]) == 1:
            return fruit[now], now
        
        best1, best2 = 0, 0
        best1Node, best2Node = now, now
        for next in graph[now]:
            if next != parent:
                f, n = dfs(now, next)
                if f > best1 or (f == best1 and n < best1Node):
                    best2, best2Node = best1, best1Node
                    best1, best1Node = f, n
                elif f > best2 or (f == best2 and n < best2Node):
                    best2, best2Node = f, n
        
        # 최대 과일 수 구하기
        total = best1 + best2 + fruit[now]
        start = min(best1Node, best2Node)
        if ans[0] < total:
            ans = [total, start]
        elif ans[0] == total:
            ans[1] = min(ans[1], start)
        
        return best1 + fruit[now], best1Node

    dfs(0, 1)
    print(*ans)

main()