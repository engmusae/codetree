N = int(input())

for i in range(1, N + 1):
    satisfied = 0
    
    for j in str(i):
        if int(j) == 3 or int(j) == 6 or int(j) == 9:
            satisfied += 1

    if i % 3 == 0:
        satisfied += 1

    if satisfied >= 1:
        print(0, end = ' ')

    else:
        print(i, end = ' ')
