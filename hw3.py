#1
lst = []

for i in range(8):
    lst.append(i**2)
print(lst)

#2
lst2 = []

for i in range(4):
    lst2.append(f'2**{i} is {2**i}')
print(lst2)

#3
lst3 = []
final_lst = []

for n in range(5,11):
    lst3.append(n)
for i in enumerate(lst3):
    final_lst.append(i)
print(final_lst)