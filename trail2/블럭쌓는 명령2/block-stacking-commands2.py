n, k = map(int, input(). split())
arr = [0] * n

for _ in range(k):
    a, b = map(int, input(). split())
    for idx in range(a, b + 1):
        arr[idx - 1] += 1

print(max(arr))