#1
lst = []

while (i := int(input('please give next int: '))) >= 0:
    lst.append(i)

print(lst)

#2
# while (i := int(input('please give next int: '))) >= 0:
#     index = 0
#     while index < len(lst) and lst[index] < i:   
#         index += 1
#     lst.insert(index, i)