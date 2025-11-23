import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    width = 4 * (N - 1) + 1
    height = 4 * (N - 1) + 3 if N > 1 else 1
    
    grid = [['*' for _ in range(width)] for _ in range(height)]
    
    def fill_layer(n, x, y):
        if n == 1:
            return
        
        width = 4 * (n - 1) + 1
        height = 4 * (n - 1) + 3
        
        # 윗변
        for i in range(width - 1):
            grid[y][x + i] = ' '
            
        # 왼변
        for i in range(height - 3):
            grid[y + i][x] = ' '
        
        # 아랫변
        for i in range(width - 3):
            grid[y + height - 3][x + i] = ' '
        
        # 오른변
        for i in range(height - 4):
            grid[y + height - i - 3][x + width - 3] = ' '
        
        fill_layer(n - 1, x + 2, y + 2)

    fill_layer(N, 1, 1)
    
    # 출력
    for i in range(height):
        if i == 1:
            print('*')
        else:
            print("".join(grid[i]))

main()