n = int(input())

cnt_g = [0] * (n + 1)
cnt_b = [0] * (n + 1)
cnt_h = [0] * (n + 1)

for i in range(1, n + 1):
    if i % 12 == 0:
        cnt_h[i] += 1
    elif i % 3 == 0:
        cnt_b[i] += 1
    elif i % 2 == 0:
        cnt_g[i] += 1

result_g, result_b, result_h = 0, 0, 0

for i in range(1, n + 1):
    if cnt_g[i] == 1:
        result_g += 1
    if cnt_b[i] == 1:
        result_b += 1
    if cnt_h[i] == 1:
        result_h += 1

print(result_g, result_b, result_h)
        
