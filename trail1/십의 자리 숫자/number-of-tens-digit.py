nums = list(map(int, input(). split()))
cnt = [0] * 9

for num in nums:
    if num != 0:
        if num // 10 > 0:
            cnt[num // 10 - 1] += 1
    else:
        break

for idx in range(len(cnt)):
    print(idx + 1, "-", cnt[idx])