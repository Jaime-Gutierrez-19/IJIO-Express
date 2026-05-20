# ─────────────────────────────────────────────────
# Usa solo int() e if — cosas que ya conocen
# ─────────────────────────────────────────────────
def redondear_arriba(numero):
    parte_entera = int(numero)
    if numero > parte_entera:   # ¿quedaron decimales?
        return parte_entera + 1
    return parte_entera

# ─────────────────────────────────────────────────
# PASO 1: Datos y conteo
# ─────────────────────────────────────────────────
puntajes = [45, 88, 72, 95, 61, 83, 39, 77, 90, 55]
total = len(puntajes)
print(f"Participantes: {total}")
# → Participantes: 10

# ─────────────────────────────────────────────────
# PASO 2: Cuántos entran en cada categoría
# ─────────────────────────────────────────────────
oro_max     = redondear_arriba(total * 0.08)  # 
plata_max   = redondear_arriba(total * 0.12)  # 
bronce_max  = redondear_arriba(total * 0.20)  # 
mencion_max = redondear_arriba(total * 0.10)  # 

print(f"Oro:     {oro_max} lugar(es)")
print(f"Plata:   {plata_max} lugar(es)")
print(f"Bronce:  {bronce_max} lugar(es)")
print(f"Mención: {mencion_max} lugar(es)")

# ─────────────────────────────────────────────────
# PASO 3: Ordenar de mayor a menor
# ─────────────────────────────────────────────────
ordenados = sorted(puntajes, reverse=True)
print(f"\nOrden: {ordenados}")

# ─────────────────────────────────────────────────
# PASO 4: Calcular cortes acumulativos
# ─────────────────────────────────────────────────
corte_oro     = oro_max                        # 1
corte_plata   = corte_oro     + plata_max      # 3
corte_bronce  = corte_plata   + bronce_max     # 5
corte_mencion = corte_bronce  + mencion_max    # 6

# ─────────────────────────────────────────────────
# PASO 5: Asignar medalla a cada posición
# ─────────────────────────────────────────────────
print("\n" + "─" * 35)
for posicion, puntaje in enumerate(ordenados):
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

    print(f"  {puntaje:3d}  (pos {posicion})  →  {medalla}")