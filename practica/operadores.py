grado = 9          # Grado escolar del estudiante
puntaje_previo = 100  # Puntaje en concurso previo
tiene_permiso = True  # ¿Tiene permiso de sus papás?

# Condición 1: ¿Está en el rango de grados?
if grado < 7 or grado > 12:
    print("❌ Grado no elegible para G7-G12")

# Condición 2: Está en rango — ¿cumple los otros requisitos?
elif puntaje_previo >= 80 and tiene_permiso:
    print("🏆 ¡Clasificado directo! Puntaje excelente.")

elif puntaje_previo >= 60 and tiene_permiso:
    print("✅ Clasificado. ¡Prepárate bien!")  # ← Este corre

elif not tiene_permiso:
    print("⚠️ Necesitas permiso de tus papás.")

else:
    print("📚 Sigue practicando, puedes lograrlo.")
