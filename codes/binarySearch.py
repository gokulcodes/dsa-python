import math
arr = []

for i in range(201):
    arr.append(i)

start = 0
x= 200
end = len(arr) - 1
def binary_search(arr, x, start, end):
    print(arr)
    while start <= end:
        mid = math.floor((start + end)/2)
        if arr[mid] == x:
            print(arr[mid])
        if arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return
binary_search(arr, x, start, end)