a, b, c = map(int, input().split())

# Please write your code here.
def sum(a, b, c):
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    return min(list)

print(sum(a, b, c))