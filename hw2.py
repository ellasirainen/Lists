lst_negative = []
lst_positive = []

while (i := int(input('give an integer: '))) > 0 or i < 0:
    if i < 0:
        lst_negative.append(i)
    elif i > 0:
        lst_positive.append(i)

if i == 0:
    print(lst_negative, lst_positive)