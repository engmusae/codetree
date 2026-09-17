age1, gen1 = input(). split()
age2, gen2 = input(). split()

if (int(age1) >= 19 and gen1 == 'M') or (int(age2) >= 19 and gen2 == 'M'):
    print('1')

else:
    print('0')