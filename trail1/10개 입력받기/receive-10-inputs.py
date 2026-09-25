nums = list(map(int, input(). split()))

sum_val = 0
yang = 0

for num in nums[:11]:
    if num != 0:
        sum_val += num
        yang += 1
    else:
        break

avg_val = sum_val / yang

print(f"{sum_val} {avg_val:.1f}")