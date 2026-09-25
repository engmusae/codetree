N, M = map(int, input(). split())
nums = list(map(int, input(). split()))

cnt = 0

for num in nums:
    if M == num:
        cnt += 1

print(cnt)
