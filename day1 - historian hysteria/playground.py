x = [1, 2, 3]
y = ['a', 'b', 'c']
z = [1j, 5 + 2j, 3 - 7j]

print(x, y, z)

for a, b, c in zip(x, y, z):
    print(f"a:{a}, b:{b}, c:{c}")


res = zip(x, y, z)
print(res)
print(type(res))
