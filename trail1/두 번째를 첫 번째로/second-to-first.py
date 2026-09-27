string = input()

for char in string:
    if char == string[1]:
        char = string[0]
    print(char, end = '')