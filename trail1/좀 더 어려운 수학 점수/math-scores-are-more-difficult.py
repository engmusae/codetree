mat_a, eng_a = map(float, input(). split())
mat_b, eng_b = map(float, input(). split())

if mat_a == mat_b:
    if eng_a > eng_b: 
        print('A')
    else:
        print('B')

else:
    if mat_a > mat_b:
        print('A')
    else:
        print('B')