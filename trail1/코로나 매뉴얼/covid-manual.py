cold1, temp1 = input(). split()
cold2, temp2 = input(). split()
cold3, temp3 = input(). split()

if (cold1 == 'Y' and cold2 == 'Y' and cold3 == 'Y'):
    if (int(temp1) >= 37 and int(temp2) >= 37) or (int(temp1) >= 37 and int(temp3) >= 37) or ((int(temp2) >= 37 and int(temp3) >= 37) or int(temp1) >= 37 and int(temp2) >= 37 and int(temp3) >= 37):
        print("E")
    else:
        print("N")

elif (cold1 == 'Y' and cold2 == 'Y'):
    if (int(temp1) >= 37 and int(temp2) >= 37):
        print("E")
    else:
        print("N")

elif (cold1 == 'Y' and cold3 == 'Y'):
    if (int(temp1) >= 37 and int(temp3) >= 37):
        print("E")
    else:
        print("N")

elif (cold2 == 'Y' and cold3 == 'Y'):
    if (int(temp2) >= 37 and int(temp3) >= 37):
        print("E")
    else:
        print("N")

else:
        print("N")