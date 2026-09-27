N = int(input())

# Please write your code here.
def hamsu(N):
    if N == 1:
        return 1

    return hamsu(N - 1) + N

print(hamsu(N))