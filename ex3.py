words = ['some', 'convenient', 'words', 'are', 'here']

# i = 0
# while i < len(words):
#     if len(words[i]) <= 4:
#         words.pop(i)
#     else:
#         i += 1

# print(words)

words = [w for w in words if len(w) > 4]
print(words)