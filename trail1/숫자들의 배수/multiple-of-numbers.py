N = int(input())

baesu = 0
for i in range(1, 50):
    print(N * i, end = ' ')
    if N * i % 5 == 0:
        baesu += 1
    if baesu == 2:
        break