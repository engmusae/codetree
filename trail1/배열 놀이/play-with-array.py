N, Q = map(int, input(). split())
arr = list(map(int, input(). split()))

for _ in range(Q):
    n_arr = list(map(int, input(). split()))
    
    if n_arr[0] == 1:
        result1 = arr[n_arr[1] - 1]
        print(result1)

    elif n_arr[0] == 2:
        if n_arr[1] in arr:
            result2 = arr.index(n_arr[1])
            print(result2 + 1)
        else:
            print(0)

    elif n_arr[0] == 3:
        s = n_arr[1]
        e = n_arr[2]
        for result3 in arr[s - 1:e]:
            print(result3, end = ' ')
        print()
    