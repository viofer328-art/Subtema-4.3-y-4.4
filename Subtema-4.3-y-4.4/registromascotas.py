import os
nombre_mascotas=[""]*3 #Lancelot
edad_mascota = [0]*3   # 3

def insertar():
    for i in range(len(nombre_mascotas)): # .Length en C#
        nombre_mascotas[i]= input(f"Ingrese nombre de la mascota: ")
        edad_mascota[i]= input (f"Ingrese la edad de la mascota: ")

def mostrar():
    print("\n--- LISTA DE MASCOTAS ---")
    for i in range(len(nombre_mascotas)):
        print(f"nombre: {nombre_mascotas[i]}, edad: {edad_mascota[i]}")

def eliminar(nombreAborrar):
    encontrado = False
    for i in range(len(nombre_mascotas)):
        if nombre_mascotas[i] == nombreAborrar: #Encuentra a la mascota que quiero borrar
            encontrado = True
            for j in range(i,len(nombre_mascotas)-1): #penúltimo registro
                # desplazando los elementos hacia la izquierda
             nombre_mascotas[j] = nombre_mascotas[j+1]
             edad_mascota[j] = edad_mascota[j+1]

             #dejar en blanco la última ubicación
             nombre_mascotas[-1] = ""
             edad_mascota[-1] = 0
             print(f"Mascota eliminada{nombre_mascotas}") # f= concatenar
             return #Detener busqueda de mascotas con el mismo nombre OPCIONAL

    if not encontrado:
        print("Mascota no encontrada.")

def ordenar():
    # Ordenamiento burbuja para mantener sincronizados los arreglos paralelos
    n = len(nombre_mascotas)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nombre_mascotas[j] > nombre_mascotas[j + 1]:
                # Intercambiar nombres
                nombre_mascotas[j], nombre_mascotas[j + 1] = nombre_mascotas[j + 1], nombre_mascotas[j]
                # Intercambiar edades correspondientes
                edad_mascota[j], edad_mascota[j + 1] = edad_mascota[j + 1], edad_mascota[j]
    print("¡Mascotas ordenadas alfabéticamente con éxito!")

def main():
    global nombre_mascotas, edad_mascota #Modificar las listas declaradas fuera del arreglo
    # arreglos paralelos ambas lisyas deben tener la misma longitud = 3
    nombre_mascotas = [""]*3 #iniciar la lista vacía para cadenas de longitud 3
    edad_mascota = [0]*3 #iniciar  la lista vacía para números enteros de longitud 3

    opcion=0
    while opcion != 4: #opción distinto a 4 (true)
        os.system('cls' if os.name == 'nt' else 'clear') #limpiar la CONSOLA
        print("[1] Insertar mascota (nombre|edad)")
        print("[2] Mostrar mascota (nombre|edad)")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] Ordenar mascotas alfabeticamente")
        print("[5] Salir")

        try:
            opcion = int(input("Elija una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            input("Presione Enter para continuar...")
            continue

        if opcion == 1:
            insertar()
        elif opcion == 2:
            mostrar()
        elif opcion == 3:
            mascotaaborrar = input("Ingrese mascota a borrar: ")
            eliminar(mascotaaborrar)
        elif opcion == 4:
            ordenar()
        elif opcion == 5:
            print("Saliendo...")
        else: 
            print("Opción inválida")
            
        if opcion != 5: 
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()