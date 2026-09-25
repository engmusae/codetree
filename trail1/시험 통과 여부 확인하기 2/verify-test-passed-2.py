N = int(input())
scores = [list(map(int, input(). split())) for _ in range(N)]

who_passed = 0
for score in scores:
    if sum(score) / 4 >= 60:
        print("pass")
        who_passed += 1
    else:
        print("fail")

print(who_passed)