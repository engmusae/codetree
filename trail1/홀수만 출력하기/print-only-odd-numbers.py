N = int(input())
arr = [int(input()) for _ in range(N)]

for a in arr:
    if a % 2 != 0 and a % 3 == 0:
        print(a)