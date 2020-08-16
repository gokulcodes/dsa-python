def main():
    n = input()
    arr = []
    for i in range(0, len(n)):
        el = input()
        arr.append(el)
    maxEl = 0
    minEl = 0
    for j in range(0, len(arr)):
        maxEl = maxEl + arr[j]


main()