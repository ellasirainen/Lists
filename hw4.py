lst = []

while (a := input('give a word: ')) != '!':
    lst.append(a)

while (b := input('give more words: ')) != '!':
    for i in lst:
        if i == b:
            print('hit')