n, m = map(int, input().split())

# Please write your code here.
def hamsu(n, m):
    lst = []
    num = min(n, m)
    result = 1

    while 0 < num <= 100:
        if n % num == 0 and m % num == 0:
            n /= num
            m /= num
            lst.append(num)
        num -= 1

    for num in lst:
        result *= num
    
    print(result)

hamsu(n, m)