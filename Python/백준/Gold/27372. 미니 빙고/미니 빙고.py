import sys, math
input = lambda: sys.stdin.readline().rstrip()

def main():
    def Find(s):
        for i in range(3):
            for j in range(3):
                if board[i][j] == s:
                    return (i, j)
    
    # i, j를 채워서 얻는 점수
    def GetScore(i, j):
        score = 0
        # 가로 확인
        for ii in range(3):
            if ii != i and fill[ii][j] == False:
                break
        else:
            score += 1
        
        # 세로 확인
        for jj in range(3):
            if jj != j and fill[i][jj] == False:
                break
        else:
            score += 1
        
        if i == j:
            for k in range(3):
                if k != i and fill[k][k] == False:
                    break
            else:
                score += 1
        
        if i + j == 2:
            for k in range(3):
                if k != i and fill[k][2-k] == False:
                    break
            else:
                score += 1
        
        return score

    def backtrack(idx):
        if idx == 9:
            return True
        
        for s, i, j in order:
            if s not in answer:
                sc = GetScore(i, j)
                if sc == TS[idx]:
                    answer.append(s)
                    fill[i][j] = True
                    if backtrack(idx+1):
                        return True
                    answer.pop()
                    fill[i][j] = False
        return False

    T = int(input())
    for _ in range(T):
        S = list(input())
        board = [list(input()) for _ in range(3)]

        fill = [[False] * 3 for _ in range(3)]
        TS = []
        order = []

        for s in S:
            i, j = Find(s)
            TS.append(GetScore(i, j))
            order.append((s, i, j))
            fill[i][j] = True
        
        order.sort()
        answer = []
        fill = [[False] * 3 for _ in range(3)]
        backtrack(0)

        print(*TS, sep='', end=' ')
        print(*answer, sep='')

main()