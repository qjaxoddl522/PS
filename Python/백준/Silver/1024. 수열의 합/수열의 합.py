N, L = map(int, input().split())

for i in range(L, 100+1):
        result = N-(i*(i+1)//2)
        if result%i == 0:
            x = result//i
            if x >= -1:
                print(' '.join(map(str,[j for j in range(x+1, x+i+1)])))
                break
else:
    print(-1)