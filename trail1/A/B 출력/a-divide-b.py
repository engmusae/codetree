A, B = map(int, input(). split())

mok1 = A // B
print(mok1, end = '.')

left = A % B * 10
for n in range(20):
    mok2 = (left // B)
    left = (left - (B * mok2)) * 10
    print(mok2, end = '')