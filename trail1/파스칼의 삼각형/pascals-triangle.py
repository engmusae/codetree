N = int(input())
arr = [[0 for num in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):

        if j == 0 or j == i:
            arr[i][j] = 1

        elif 0 < j < i:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

        if arr[i][j] != 0:
            print(arr[i][j], end = ' ')
    print()