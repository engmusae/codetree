str1 = input()
str2 = input()
str3 = input()

length = [len(str1), len(str2), len(str3)]

max_len = max(length)
min_len = min(length)

print(max_len - min_len)