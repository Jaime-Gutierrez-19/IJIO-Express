def redondear_arriba(numero):
    parte_entera = int(numero)      # int(0.8) = 0  / int(2.0) = 2
    if numero > parte_entera:       # ¿quedaron decimales?
        return parte_entera + 1     # sube uno
    return parte_entera             # ya era entero exacto


#(1) contar cuántos participantes hay
puntajes = [45, 88, 72, 95, 61, 83, 39, 77, 90, 55, 65, 100 , 80, 90, 70, 30, 20, 0]
total = len(puntajes)
print(f"Participantes: {total}")

#(2) calcular cuántos corresponden a cada categoría
oro_max     = redondear_arriba(total * 0.08)  # 
plata_max   = redondear_arriba(total * 0.12)  # 
bronce_max  = redondear_arriba(total * 0.20)  # 
mencion_max = redondear_arriba(total * 0.10)  # 

print(f"Oro:     {oro_max} lugar(es)")
print(f"Plata:   {plata_max} lugar(es)")
print(f"Bronce:  {bronce_max} lugar(es)")
print(f"Mención: {mencion_max} lugar(es)")

#(3) ordenar los puntajes de mayor a menor
ordenados = sorted(puntajes, reverse=True)
print(f"\nOrden: {ordenados}")

#(4) asignar medalla a cada participante e imprimirlo

corte_oro     = oro_max                        # 1
corte_plata   = corte_oro     + plata_max      # 3
corte_bronce  = corte_plata   + bronce_max     # 5
corte_mencion = corte_bronce  + mencion_max    # 6

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

  print(f" {puntaje:3d} (pos {posicion}) → {medalla}")