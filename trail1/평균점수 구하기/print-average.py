scores = list(map(float, input(). split()))

sum_val = sum(scores)
avg_val = sum_val / len(scores)

print(f"{avg_val:.1f}")