n = int(input())
arr = [0] * 100

for _ in range(n):
    x1, x2 = map(int, input(). split())

    for idx in range(x1, x2 + 1):
        arr[idx - 1] += 1

print(max(arr))