def f(lista):
    return [x**2 for x in lista if x % 2 == 0]

print(f([1, 2, 3, 4, 5, 6]))