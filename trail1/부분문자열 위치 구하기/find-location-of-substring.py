input_str = input()
target_str = input()

# Please write your code here.
if target_str in input_str:
    for i in range(len(input_str)):
        if target_str == input_str[i:i + len(target_str)]:
            print(i)
            break

else:
    print(-1)