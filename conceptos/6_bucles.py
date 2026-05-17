#for (usado mucho para iterar rangos)

for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (salto de 2)
    print(i)

#while

n = 5
while n > 0:
    print(n)
    n -= 1

#break y continue
for i in range(10):
    if i == 5:
        break       # sale del bucle
    if i % 2 == 0:
        continue    # salta esta iteración
    print(i)
