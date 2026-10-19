grid = [[0] * 2000 for _ in range(2000)]

for _ in range(3):
    if _ == 2:
        x1, y1, x2, y2 = map(int, input(). split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                grid[i + 1000][j + 1000] = 0

    else:
        x1, y1, x2, y2 = map(int, input(). split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                grid[i + 1000][j + 1000] = 1

result = 0
for i in range(2000):
    for j in range(2000):
        if grid[i][j] == 1:
            result += 1
print(result)