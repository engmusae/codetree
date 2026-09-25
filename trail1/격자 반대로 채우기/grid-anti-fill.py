N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

num = 1
for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            arr[N - 1 - j][N - 1 - i] = num
        else:
            arr[j][N - 1 - i] = num
        num += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = ' ')
    print()