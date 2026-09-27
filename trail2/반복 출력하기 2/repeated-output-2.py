n = int(input())

# Please write your code here.
def hamsu(n):
    if n == 0:
        return
    else:
        hamsu(n - 1)
        print('HelloWorld')

hamsu(n)