arr = list(map(int, input(). split()))

n = 0
sum_val = 0

for num in arr:      
    if n <= 10: 
        n += 1                   
        if num < 250:
            sum_val += num
        else:
            break
    avg_val = sum_val / n

print(f"{sum_val} {avg_val:.1f}")