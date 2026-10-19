n = int(input())
arr = [int(input()) for _ in range(n)]
result = []

for idx in range(n):
    if idx == 0 or arr[idx] != arr[idx - 1]:
        cnt = 1
    elif arr[idx] == arr[idx - 1]:
        cnt += 1
    result.append(cnt)

print(max(result))