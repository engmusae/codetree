arr = list(map(int, input(). split()))

cnt = 0
sum_val = 0

for num in arr:
    if num != 0:
        if num % 2 == 0:
            cnt += 1
            sum_val += num
    else:
        break

print(cnt, sum_val)