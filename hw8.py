lst = []
lst_res = []
while (a := input('give a word: ')) != '!':
    lst.append(a)
    lst_res.append(a)

lst_indices = []
while (b := int(input('give an index: '))) >= 0:
    lst_indices.append(b)

for (i, w) in enumerate(lst):
    for l in lst_indices:
            if i == l:
                 lst_res.remove(w)

print(f'original: {lst}')
print(f'indices: {lst_indices}')
print(f'result: {lst_res}')

