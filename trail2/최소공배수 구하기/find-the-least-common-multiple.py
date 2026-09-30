n, m = map(int, input().split())

# Please write your code here.
list = []
num = 100
result = 1

while num > 0:
    if n % num == 0 and m % num == 0:
        n /= num
        m /= num
        list.append(num)
    num -= 1

list.append(n)
list.append(m)

for i in list:
    result *= i

print(int(result))