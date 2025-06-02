def fivo(arr, n):
    if len(arr)-1 < n:
        arr.append(arr[len(arr)-2] + arr[len(arr)-1])
        return fivo(arr, n)
    else:
        return arr[n]
n = int(input())
print(fivo([0, 1], n))