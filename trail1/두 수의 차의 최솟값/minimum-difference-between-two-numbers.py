N = int(input())
arr = list(map(int, input(). split()))

min_cha = abs(arr[0] - arr[1])
for idx in range(N):
    for i in range(idx + 1, N):
        cha = abs(arr[idx] - arr[i])
        if min_cha > cha:
            min_cha = cha

print(min_cha)