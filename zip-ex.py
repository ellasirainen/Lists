t = (2, 'text') # tuple with two elements
print(t)
print(len(t))
(num, word) = t # unpacking elements
print(num, word)

quantity = [34, 5, 19, 18, 82]
unit_price = [81.3, 44, 71.3, 113, 8.4]

# traverse columns
for p in zip(quantity, unit_price): print(p)

# calculate total price
total_price = 0
for (q, p) in zip(quantity,  unit_price):
    total_price += q * p
print(total_price)