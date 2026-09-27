n = int(input())

# Please write your code here.
def hamsu(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    result = sum // 10
    return result

print(hamsu(n))