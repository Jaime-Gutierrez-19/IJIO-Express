import math

puntajes = [45, 88, 72, 95, 61, 83, 39, 77, 90, 55]

# ── PASO 1: Contar participantes ──────────────────────────────
total = len(puntajes)
print(f"Participantes: {total}")
# → 10

# ── PASO 2: Calcular cuántos entran en cada categoría ────────
# math.ceil redondea HACIA ARRIBA  (ceil(0.8) = 1, no 0)
# max(1, ...) garantiza que SIEMPRE al menos 1 persona gana
oro_max     = max(1, math.ceil(total * 0.08))   # ceil(0.8)  = 1
plata_max   = max(1, math.ceil(total * 0.12))   # ceil(1.2)  = 2
bronce_max  = max(1, math.ceil(total * 0.20))   # ceil(2.0)  = 2
mencion_max = max(1, math.ceil(total * 0.10))   # ceil(1.0)  = 1

print(f"Oro     (8%)  → {oro_max} lugar(es)")
print(f"Plata   (12%) → {plata_max} lugar(es)")
print(f"Bronce  (20%) → {bronce_max} lugar(es)")
print(f"Mención (10%) → {mencion_max} lugar(es)")
print()

# ── PASO 3: Ordenar de MAYOR a MENOR ────────────────────────
puntajes_ordenados = sorted(puntajes, reverse=True)
print("Orden:", puntajes_ordenados)
# → [95, 90, 88, 83, 77, 72, 61, 55, 45, 39]
print()

# ── PASO 4: Calcular los CORTES ACUMULATIVOS ────────────────
# Cada corte es la posición HASTA DONDE llega cada medalla
corte_oro     = oro_max                                          # 1
corte_plata   = oro_max + plata_max                              # 3
corte_bronce  = oro_max + plata_max + bronce_max                 # 5
corte_mencion = oro_max + plata_max + bronce_max + mencion_max   # 6

# ── PASO 5: Recorrer y asignar ───────────────────────────────
print("─" * 32)
for posicion, puntaje in enumerate(puntajes_ordenados):
    if posicion < corte_oro:
        medalla = "🥇 ORO"
    elif posicion < corte_plata:
        medalla = "🥈 PLATA"
    elif posicion < corte_bronce:
        medalla = "🥉 BRONCE"
    elif posicion < corte_mencion:
        medalla = "🏅 MENCIÓN HONORÍFICA"
    else:
        medalla = "📜 CERTIFICADO"

    print(f"{puntaje:3d} (posición {posicion}) → {medalla}")