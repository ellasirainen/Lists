lst = []
while (n := int(input('give an integer: '))) >= 0:
    lst.append(n)
    for i in lst:
        if i not in lst:
            lst.insert(0, i)
        else:
            lst.remove(i)
            lst.insert(0,i)
print(lst)