# Línea 1: Guardamos la temperatura en una variable
temperatura = input("cual es tu temperatura?")

# Línea 3: Preguntamos: ¿es temperatura mayor a 36.5?
if temperatura > 36.5:
    # Línea 5: Esto corre porque 38 > 36.5 es TRUE
    print("🌡️ ¡Tienes fiebre! Ve al médico.")
else:
    # Esta parte NO corre porque el if fue True
    print("✅ Tu temperatura es normal.")

