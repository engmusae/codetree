n = int(input())
grid = [[0] * 200 for _ in range(200)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input(). split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i + 100][j + 100] += 1

result = 0
for i in range(200):
    for j in range(200):
        if grid[i][j] >= 1:
            result += 1
print(result)