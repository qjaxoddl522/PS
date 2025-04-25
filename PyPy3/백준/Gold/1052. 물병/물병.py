N, K = map(int, input().split())

bottle = 0

while bin(N).count('1') > K:
    index = bin(N)[::-1].index('1')
    bottle += 2**index
    N += 2**index
    
print(bottle)
