
import os
nombre_mascotas=[""]*3
edad_mascota = [0]*3

def insertar():
    for i in range(len(nombre_mascotas)):
        nombre_mascotas[i]= input(f"Ingrese nombre de la mascota: ")
        edad_mascota[i]= input (f"Ingrese la edad de la mascota: ")

def mostrar():
    for i in range(len(nombre_mascotas)):
        print(f"nombre: {nombre_mascotas[i]}, edad: {edad_mascota[i]}")


def main():
    global nombre_mascotas, edad_mascota

    nombre_mascotas = [""]*3
    edad_mascota = [0]*3

    opcion=0
    while opcion != 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[1] Insertar mascota (nombre|edad)")
        print("[2] Mostrar mascota (nombre|edad)")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] Salir")
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            insertar()
        elif opcion == 2:
            print("Mostrar")
        elif opcion == 3:
            print("Eliminar")
        elif opcion == 4:
            print("Saliendo...")
        else: print("Opción inválida")
        if opcion != 4: input("Presione para continuar")

main()
