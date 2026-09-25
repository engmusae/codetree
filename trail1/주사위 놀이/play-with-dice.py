nums = list(map(int, input(). split()))
cnt = [0] * 6

for num in nums:
    cnt[num - 1] += 1

for idx in range(len(cnt)):
    print(idx + 1, "-", cnt[idx])