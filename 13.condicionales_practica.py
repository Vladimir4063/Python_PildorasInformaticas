print("Asignaturas optativas Año 2021")
text = """
Informática gráfica - Pruebas de Software - Usabilidad y Accesibilidad
"""

print(text)
opc = (input("Escribe la asignatura: "))

asignatura = opc.lower()  # Convierte cualquier Mayú en Minú, para evaluar.

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("Asignatura no contemplada.")
