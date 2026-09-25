arr = [list(input(). split()) for _ in range(5)]

for row in arr:
    result = [r.upper() for r in row]
    print(*result)