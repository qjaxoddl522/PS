import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(9999)

"""
역의 수와 경로 수가 같기 때문에 순환선은 반드시 하나
모든 역이 연결되어 있으므로 1번에서 시작해 방문을 확인하여 아무 시작점 찾기
"""
def main():
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(N):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    
    # 아무 시작점 찾기
    visited = [False] * (N+1)
    # (현재노드, 부모노드)
    stack = [(1, -1)] 
    startNode = None
    while stack:
        node, parent = stack.pop()
        
        if not visited[node]:
            visited[node] = True
            
            for nNode in graph[node]:
                if nNode == parent:
                    continue
                # 순환 발견
                if visited[nNode]:
                    startNode = nNode
                    break
                else:
                    stack.append((nNode, node))
    
    # 백트래킹으로 순환선 찾기
    dist = [-1] * (N+1)
    path = [startNode]
    visited = [False] * (N+1)
    def dfs(node):
        for nNode in graph[node]:
            # 시작 직후가 아니고 다음이 시작노드여야 순환
            if len(path) > 2 and nNode == startNode:
                for n in path:
                    dist[n] = 0
            if not visited[nNode]:
                visited[nNode] = True
                path.append(nNode)
                dfs(nNode)
                visited[nNode] = False
                path.pop()
    visited[startNode] = True
    dfs(startNode)
    
    def dfss(node):
        for nNode in graph[node]:
            if dist[nNode] == -1:
                dist[nNode] = dist[node] + 1
                dfss(nNode)
    
    for i in range(1, N+1):
        if dist[i] == 0:
            dfss(i)
    
    print(*dist[1:])

main()