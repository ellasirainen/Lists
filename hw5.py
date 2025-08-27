lst = []
lst2 = []
while (n := int(input('give an integer: '))) >= 0:
    lst.append(n)
    for i in lst:
        if i not in lst2:
            lst2.append(i)
print(lst)
print(lst2)