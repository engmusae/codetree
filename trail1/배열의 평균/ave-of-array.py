arr = [list(map(int, input(). split())) for _ in range(2)]

for row in arr:
    avg_row = sum(row) / len(row)
    print(f"{avg_row:.1f}", end = ' ')

print()

for i in range(len(arr[0])):
    sum_col = 0
    for j in range(len(arr)):
        sum_col += arr[j][i]
    avg_col = sum_col / 2
    print(f"{avg_col:.1f}", end = ' ')

print()

sum_elem = 0
elems = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        sum_elem += arr[i][j]
        elems += 1
print(f"{sum_elem / elems:.1f}")