N = int(input())
scores = list(map(float, input(). split()))

sum_scores = sum(scores)
avg_scores = sum_scores / len(scores)

print(f"{avg_scores:.1f}")
if avg_scores >= 4.0:
    print("Perfect")
elif avg_scores >= 3.0:
    print("Good")
else:
    print("Poor")