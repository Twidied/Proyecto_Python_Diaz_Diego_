score = (["🤮🤡 BAJO", 0, 25], ["💁🥱 ACEPTABLE", 26, 50], ["🥳💃 SOBRESALIENTE", 51, 80], ["🔝👑 EXCELENTE", 81, 100])


def funcion(nota):
    for i, n in enumerate(score, start= 1):
        if(nota >= n[1] and nota <= n[2]):
            print(f"la nota es 👰: {i} - {n[0]}")
            break

def promedios():
    mensaje = " 📚📄 Notas: \n"
    for i, n in enumerate(score, start = 1):
        nombre = n[0]
        min = n[1]
        max = n[2]


        mensaje += promedioNota(posicion= i, Nombre= nombre, rango= [min, max]) + "\n"
        #mensaje += f"{i}. {n[1]} a {n[2]} -> {n[10]} \n"
    return mensaje
    
    
def promedioNota(posicion: int, Nombre: str, rango: list):
    return f"{posicion}. {rango[0]} a {rango[1]} -> {Nombre}"


nota = float(input("ingrese la nota 📥🩴: "))
print(promedios())
funcion(nota)

