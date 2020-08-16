arr = [4,3,4,1,4]

# Bubble Sort
def bubble(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
# bubble(arr)

# Selection Sort
def selection(arr):
    n = len(arr)
    for i in range(0, n):
        lower = i
        for j in range(i+1, n):
            if arr[j] > arr[lower]:
                lower = j
        if i != n:
            arr[i], arr[lower] = arr[lower], arr[i]

    print(arr)
# selection(arr)

# Insertion Sort
def insertion(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while current < arr[j] and j >= 0:
            arr[j+1] = arr[j] 
            j = j - 1
        arr[j+1] = current
    print(arr)

# insertion(arr)


def duplicates(arr):
    x = arr[0]
    n = len(arr)
    for i in range(0, n):
        if arr[0] == arr[i]
           print('duplicate found')
        else: 
            print('not found') 

duplicates(arr)