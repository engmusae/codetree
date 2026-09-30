n = int(input())

# Please write your code here.
def check(n):
    first = n // 10
    second = n % 10
    return n % 2 == 0 and (first + second) % 5 == 0

if check(n) == True:
    print("Yes")

else:
    print("No")