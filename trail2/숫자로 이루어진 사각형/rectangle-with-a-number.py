n = int(input())

# Please write your code here.
def hamsu(n):
    arr = [[0 for _  in range(n)] for _ in range(n)]

    num = 1
    for i in range(n):
        for j in range(n):
            arr[i][j] = num
            num += 1
            if num == 10:
                num = 1

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')            
        print()

hamsu(n)