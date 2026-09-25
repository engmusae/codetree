N, M = map(int, input(). split())
arr1 = [list(map(int, input(). split())) for _ in range(N)]
arr2 = [list(map(int, input(). split())) for _ in range(N)]
arr = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr1[i][j] == arr2[i][j]:
            arr[i][j] = 0
        else:
            arr[i][j] = 1
        print(arr[i][j], end = ' ')
    print()