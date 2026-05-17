#Conversión entre bases (binario, decimal, hexadecimal)

# Decimal a binario (algoritmo manual)
def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario

# Binario a decimal
def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in reversed(binario):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    return decimal

# Versión rápida con funciones integradas
binario = bin(25)[2:]         # '11001' (quitar '0b')
decimal = int("11001", 2)     # 25
hexadecimal = hex(25)[2:].upper()  # '19'

#Números primos

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#Máximo Común Divisor (MCD) - Algoritmo de Euclides

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Factorial
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

#Contar dígitos, invertir números, suma de dígitos

def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

def invertir_numero(n):
    inverso = 0
    while n > 0:
        inverso = inverso * 10 + n % 10
        n //= 10
    return inverso

