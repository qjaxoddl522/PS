def han(n):
    ar = list(map(int, str(n)))
    if len(ar) <= 2:
        return True
    else:
        for i in range(2, len(ar)):
            streak = ar[0]-ar[1]
            if streak != ar[i-1]-ar[i]:
                return False
        return True
count = 0
for i in range(1, int(input())+1):
    if han(i):
        count += 1
print(count)