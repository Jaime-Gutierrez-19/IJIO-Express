# Listas (Estructura de datos más usada)

# Creación
arr = [1, 2, 3, 4, 5]
arr2 = list(range(10))  # [0, 1, 2, ..., 9]

# Acceder
print(arr[0])      # 1 (índice empieza en 0)
print(arr[-1])     # 5 (último elemento)

# Modificar
arr[0] = 10

# Agregar
arr.append(6)
arr.insert(0, 0)   # insertar en posición 0

# Longitud
print(len(arr))

# Recorrer
for x in arr:
    print(x)

# Porciones (slicing)
print(arr[1:4])    # [2, 3, 4]
print(arr[::-1])   # invertir lista [web:21]