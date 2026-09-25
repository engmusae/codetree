nums = list(map(int, input(). split()))

result = []
for num in nums:
    if num != 0:
        result.append(num)
    elif num == 0:
        break

for num in result[::-1]:
    print(num, end = ' ')

