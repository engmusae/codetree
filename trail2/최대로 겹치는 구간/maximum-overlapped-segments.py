N = int(input())
arr = [0] * 200
for _ in range(N):
    x1, x2 = map(int, input(). split())

    for idx in range(x1, x2):
        arr[idx + 100] += 1

print(max(arr))