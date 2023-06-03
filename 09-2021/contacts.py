contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Bob', 18)
]

name = input()

for x in contacts: #makes a x go through contacts list
    if name in x:
        print(str(x[0]) + "is" + str(x[1]))
        break
    else:
        print("not found")