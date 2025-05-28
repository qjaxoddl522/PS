import copy

B = int(input())
board = [list(input().strip()) for _ in range(B)]

def bubble_sort(K):
    original = copy.deepcopy(K)
    total = 1
    n = len(K)
    
    for i in range(n):
        for j in range(n-1):
            if K[i][j] != K[i][j+1]:
                K[i][j], K[i][j+1] = K[i][j+1], K[i][j]
                total = max(total, solve_board(K))
                K[:] = copy.deepcopy(original)[:]
    
    for j in range(n):
        for i in range(n-1):
            if K[i][j] != K[i+1][j]:
                K[i][j], K[i+1][j] = K[i+1][j], K[i][j]
                total = max(total, solve_board(K))
                K[:] = copy.deepcopy(original)[:]
    return total

def solve_board(K):
    RVS = list(map(list, zip(*K)))
    return max(check(K, B), check(RVS, B))

#연속된 걸 찾는 함수
def check(K, n):
    max_len = 0
    for i in range(n):
        cnt = 1  # 각 행마다 초기화
        for j in range(1, n):
            if K[i][j] == K[i][j-1]:
                cnt += 1
            else:
                max_len = max(max_len, cnt)
                cnt = 1
        max_len = max(max_len, cnt)  # 행의 끝에서의 연속 길이 체크
    return max_len

res = bubble_sort(board)

print(res)