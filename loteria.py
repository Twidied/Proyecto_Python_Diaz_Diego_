import os
import json
import random

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


print("""
+__________________________________________________________________________________________________________________________________________________+
⌇     ⋆              ⋆              ⋆                                                                                                               ⌇
⌇                                               ⋆                       ⋆               ⋆           ⋆                ⋆                      ⋆       ⌇
⌇            ⋆               ⋆   ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗                       ⋆                ⌇
⌇   ⋆               ⋆            ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗          ⋆                        ⋆   ⌇
⌇                                ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║                                       ⌇
⌇                                ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║                                 ⋆     ⌇
⌇          ⋆          ⋆          ██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝⋆          ⋆            ⋆              ⌇
⌇                                ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝                                        ⌇
⌇        ⋆                     ⋆          ⋆                    ░█▀█░░░█▄█░▀█▀                   ⋆                                                   ⌇
⌇                                                  ⋆           ░█▀█░░░█░█░░█░      ⋆                     ⋆          ⋆         ⋆         ⋆           ⌇
⌇   ⋆                ⋆                                         ░▀░▀░░░▀░▀░▀▀▀            ⋆       ⋆                                                  ⌇
⌇       ⋆                                   ██╗      ██████╗ ████████╗███████╗██████╗ ██╗ █████╗⋆     ⋆         ⋆                              ⋆    ⌇
⌇ ⋆                                         ██║     ██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗██║██╔══██╗                                                   ⌇
⌇                             ⋆        ⋆    ██║     ██║   ██║   ██║   █████╗  ██████╔╝██║███████║           ⋆                ⋆            ⋆         ⌇
⌇            ⋆                              ██║     ██║   ██║   ██║   ██╔══╝  ██╔══██╗██║██╔══██║                                                   ⌇
⌇                         ⋆                 ███████╗╚██████╔╝   ██║   ███████╗██║  ██║██║██║  ██║                   ⋆                               ⌇
⌇   ⋆                               ⋆       ╚══════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝   ⋆                        ⋆            ⋆         ⌇
⌇          ⋆             ⋆                 ⋆           ⋆                 ⋆           ⋆                      ⋆           ⋆                           ⌇
+__________________________________________________________________________________________________________________________________________________+
""")

input("presiona enter para continuar")
limpiar_pantalla()


def comprar_boletos():
    limpiar_pantalla()
    
    print("""
░█▀▀░█▀█░█▄█░█▀█░█▀▄░█▀█░░░█▀▄░█▀▀░░░█▀▄░█▀█░█░░░█▀▀░▀█▀░█▀█░█▀▀░░░░
░█░░░█░█░█░█░█▀▀░█▀▄░█▀█░░░█░█░█▀▀░░░█▀▄░█░█░█░░░█▀▀░░█░░█░█░▀▀█░░░░
░▀▀▀░▀▀▀░▀░▀░▀░░░▀░▀░▀░▀░░░▀▀░░▀▀▀░░░▀▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░░░░
""")
    while True:
        titular = input("Ingresa el nombre del titular del boleto: ")
        if titular == "":
            print("El nombre no puede estar vacio. Intentalo de nuevo.")
        elif any(char.isdigit() for char in titular):
            print("El nombre no puede contener numeros. Intentalo nuevamente.")
        else:
            break

    numeros_usados = set()
    historial_path = "historial_usuario.json"
    try:
        with open("historial_usuario.json", "r", encoding="utf-8") as archivo:
            historial = json.load(archivo)
            for item in historial:
                numeros_usados.add(item["boleto"])
    except (FileNotFoundError, json.JSONDecodeError):
        historial = []

    while True:
        entrada = input("Ingrese un numero valido entre 0 y 99999: ").strip()

        if not entrada.isdigit():
            print("Por favor, ingrese un numero entero valido.")
            continue

        boleto_num = int(entrada)

        if boleto_num in numeros_usados:
            print("Este numero ya fue comprado. Por favor ingresa otro.")
            continue

        if 0 <= boleto_num <= 99999:
            boleto = {
            "Titular": titular,
            "boleto": boleto_num
            }
            historial.append(boleto)

            with open(historial_path, "w", encoding="utf-8") as archivo:
                json.dump(historial, archivo, ensure_ascii=False, indent=4)

            print("Boleto registrado exitosamente.")
            input("Presiona ENTER para continuar...")
            break
        else:
            print("El numero debe estar entre 0 y 99999. Intenta nuevamente.")

def mostrar_historial():
    print("Aqui esta tu historial de compras:\n")
    historial_path = "historial_usuario.json"

    if not os.path.exists(historial_path):
        print("No se encontro ningun historial de compras.")
    else:
        with open(historial_path, "r", encoding="utf-8") as archivo:
            try:
                historial = json.load(archivo)
                if not historial:
                    print("aun no hay compras registradas")
                else:
                    for boleto in historial:
                        print(f"Titular: {boleto['Titular']}")
                        print(f"Boleto: {boleto['boleto']:05}")
                        print("-" * 30)
            except json.JSONDecodeError:
                input("no se pudo cargar correctamente el hisorial")
    input("presiona ENTER para continuar.")
    limpiar_pantalla()




def numeros_aleatorios():
    while True:
        try:
            numero_ganador = random.randint(0, 99999)
            return numero_ganador 
        except Exception as e:
            print("no se pudo generar el numero ganador:", e)
            return None



def verificar_premios(numero_ganador):
    try:
        with open("historial_usuario.json", "r", encoding="utf-8") as archivo:
            mostrar_historial = json.load(archivo)

        print(f"\nNUMERO GANADOR: {numero_ganador:05}")
        print("RESULTADOS DE LOS BOLETOS COMPRADOS:\n")

        for boleto in mostrar_historial:
            numero = str(boleto["boleto"]).zfill(5)
            ganador = str(numero_ganador).zfill(5)

            aciertos = sum(1 for i in range(5) if numero[i] == ganador[i])

            if aciertos == 5:
                premio = "🌟 Premio mayor"
            elif aciertos == 4:
                premio = "✨ Premio grande"
            elif aciertos == 3:
                premio = "🎯 Premio mediano"
            elif aciertos == 2:
                premio = "🎁 Premio pequeño"
            else:
                premio = "😐 Sin premio"

            boleto_str = str(boleto['boleto']).zfill(5)
            print(f"Titular: {boleto['Titular']:<5} Boleto: {str(boleto['boleto']).zfill(5)}  Aciertos: {aciertos:<2}  Premio: {premio}")
    except FileNotFoundError:
        print("⚠️ No se encontro el archivo 'historial_usuario.json'. Asegurate de haber comprado boletos.")
    except Exception as e:
        print(f"Error al verificar premios: {e}")
    input("\nPresiona ENTER para continuar...")


def ver_explicacion_premios():
    limpiar_pantalla()

    print("""      
          
                  ░█▀█░█▀▄░█▀▀░█▄█░▀█▀░█▀█░█▀▀
                  ░█▀▀░█▀▄░█▀▀░█░█░░█░░█░█░▀▀█
                  ░▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀
          
                  🌟 5 aciertos → Premio mayor
                  ✨ 4 aciertos → Premio grande
                  🎯 3 aciertos → Premio mediano
                  🎁 2 aciertos → Premio pequeño
                  😐 0-1 aciertos → Sin premio
""")
    input("Presiona ENTER para volver al menu...")



def chau():
    try:
        limpiar_pantalla()
        print("""
+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+.+º+.+º+º+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.  
|                                                                                                                                                |
|                           █████████  ███████████     █████████     █████████  █████   █████████       █████████ ███                            |
|                          ███░░░░░███░░███░░░░░███   ███░░░░░███   ███░░░░░███░░███   ███░░░░░███   ███░░░░░███ ░███                            |
|                         ███     ░░░  ░███    ░███  ░███    ░███  ███     ░░░  ░███  ░███    ░███  ░███    ░░░  ░███                            |
|                        ░███          ░██████████   ░███████████ ░███          ░███  ░███████████  ░░█████████  ░███                            |
|                        ░███    █████ ░███░░░░░███  ░███░░░░░███ ░███          ░███  ░███░░░░░███   ░░░░░░░░███ ░███                            |
|                        ░░███  ░░███  ░███    ░███  ░███    ░███ ░░███     ███ ░███  ░███    ░███   ███    ░███ ░░░                             |
|                         ░░█████████  █████   █████ █████   █████ ░░█████████  █████ █████   █████ ░░█████████   ███                            |
|                          ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░   ░░░░░   ░░░░░░░░░  ░░░░░ ░░░░░   ░░░░░    ░░░░░░░░░   ░░░                            |
|                                                                                                                                                |
|                                       ░█░█░█▀█░█▀▀░▀█▀░█▀█░░░█░░░█▀█░░░█▀█░█▀▄░█▀█░█░█░▀█▀░█▄█░█▀█                                             |
|                                       ░█▀█░█▀█░▀▀█░░█░░█▀█░░░█░░░█▀█░░░█▀▀░█▀▄░█░█░▄▀▄░░█░░█░█░█▀█                                             |
|                                       ░▀░▀░▀░▀░▀▀▀░░▀░░▀░▀░░░▀▀▀░▀░▀░░░▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀                                             |
|                                                                                                                                                |
+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+.+º+.+º+º+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.+º+.
""")
    except  Exception:
        print("\nNo c\n")
        input("Presiona Enter para salir")



def menu():
    while True:
        try:
            limpiar_pantalla()
            print("""
__________________________________________________________________________________________________________________________________________________
|                               ⋆                                                                               ⋆         ⋆                    ⋆  |
|           ⋆                              ██████   ██████ ██████████ ██████   █████ █████  █████                                     ⋆           |
| ⋆                   ⋆          ⋆        ░░██████ ██████ ░░███░░░░░█░░██████ ░░███ ░░███  ░░███       ⋆         ⋆          ⋆                     |
|                                          ░███░█████░███  ░███  █ ░  ░███░███ ░███  ░███   ░███                                            ⋆     |  
|           ⋆                ⋆             ░███░░███ ░███  ░██████    ░███░░███░███  ░███   ░███                     ⋆           ⋆                |
| ⋆                    ⋆           ⋆       ░███ ░░░  ░███  ░███░░█    ░███ ░░██████  ░███   ░███       ⋆                                          |
|                                          ░███      ░███  ░███ ░   █ ░███  ░░█████  ░███   ░███               ⋆           ⋆              ⋆       |
|                ⋆                         █████     █████ ██████████ █████  ░░█████ ░░████████                                                   |
|        ⋆                 ⋆          ⋆    ░░░░░     ░░░░░ ░░░░░░░░░░ ░░░░░    ░░░░░   ░░░░░░░░      ⋆            ⋆         ⋆       ⋆             |
|                                                                                                                                                 |
|     ⋆       ⋆             ⋆            ⋆            ⋆                  ⋆                  ⋆                      ⋆           ⋆                  |
|                                                               1.COMPRAR BOLETOS                                                          ⋆      |
|                   ⋆              ⋆             ⋆          ⋆   2.SORTEO VIRTUAL                     ⋆                                            |
|       ⋆                                                       3.HISTORIAL        ⋆           ⋆                      ⋆               ⋆           |                                                                  
|    ⋆                                ⋆             ⋆           4.PREMIOS                                                                         |
|                ⋆         ⋆              ⋆                     5.SALIR    ⋆                                    ⋆                 ⋆               |
|_________________________________________________________________________________________________________________________________________________|
 """)

            opcion = input("ingresa el numero de lo que quieras realizar: ")

            if opcion == "1":
                comprar_boletos()
                limpiar_pantalla()
            elif opcion == "2":
                numero_ganador = numeros_aleatorios()
                verificar_premios(numero_ganador)

                limpiar_pantalla()
            
            elif opcion == "3":
                mostrar_historial()
                limpiar_pantalla()
            elif opcion == "4":
                ver_explicacion_premios()
                limpiar_pantalla()

            elif opcion == "5":
                chau()
                print("saliendo...")
                break
            else:
                print("Incorrecto. Esa opcion no existe 😕")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
menu()
