import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    parents = list(map(int, input().split()))
    
    tree = [[] for _ in range(N)]
    
    for i, p in enumerate(parents):
        if p >= 0:
            tree[p].append(i)
    
    def dfs(u):
        if not tree[u]:
            return 0
        
        # 모든 자식 노드에 대해 걸리는 시간 계산하고 오래 걸리는 순서대로 정렬
        child_times = []
        for v in tree[u]:
            child_times.append(dfs(v))
        child_times.sort(reverse=True)
        
        # 각 자식에게 전화를 거는 순서를 고려하여 최대 시간 계산
        max_time = 0
        for i, time in enumerate(child_times):
            # (i+1)은 대기 시간 및 통화 시간, time은 자식의 서브트리 소요 시간
            max_time = max(max_time, time + (i + 1))
        
        return max_time

    print(dfs(0))

main()