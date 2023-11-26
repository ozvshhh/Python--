imoge = input()

colon = 0
under_bar = 0
for char in imoge:
    if char == ":":
        colon += 1
    if char == "_":
        under_bar += 1

diff = len(imoge)+colon+under_bar*5
print(diff)