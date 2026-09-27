N = int(input())
arr = [input() for _ in range(N)]
char = input()

cnt = 0
length = 0

for string in arr:
    if char == string[0]:
        cnt += 1
        length += len(string)

print(f"{cnt} {length / cnt:.2f}")