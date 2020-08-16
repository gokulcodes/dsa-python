
def main():
    n = input()
    arr = []
    for i in range(0, int(n)):
        finder = input()
        arr.append(finder)

    for k in range(0, len(arr)):
        for j in range(1, int(arr[k])):
            if int(arr[k]) % j == 0:
                temp = j
                temp = temp + j
        if temp == int(arr[k]):
            print("YES")
        else:
            print('NO')

main()