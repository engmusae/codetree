n, m = map(int, input().split())

# Please write your code here.
def hamsu(n, m):
    for _ in range(n):
        for _ in range(m):
            print(1, end = '')
        print()

hamsu(n, m)