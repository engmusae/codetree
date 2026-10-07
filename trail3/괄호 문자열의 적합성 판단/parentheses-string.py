str = input()

# Please write your code here.

stack = []
result = 1

for s in str:
    if len(stack) == 0:
        if s == ')':
            result = 0
            break
        else:
            stack.append(s)
    elif len(stack) >= 1:
        stack.append(s)
        if s == ')':
            stack.pop()
            stack.pop()

if len(stack) != 0:
    result = 0

if result == 0:
    print('No')
else:
    print('Yes')