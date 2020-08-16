def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        lowest = i
        for j in range(i+1, n):
            if arr[j] < arr[lowest]:
                lowest = j
        if i != n:
            arr[i], arr[lowest] = arr[lowest], arr[i]
    print(arr)
selectionSort([4,2,8,1,12,6])