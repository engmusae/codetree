N = int(input())
nums = list(map(int, input(). split()))
cnt = [0] * 9

for num in nums:
    cnt[num - 1] += 1

for result in cnt:
    print(result)