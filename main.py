import os
import time

def menu():
    print("Bienvenido a la agenda de contactos")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Cargar contactos desde archivo")
    print("7. Guardar contactos en archivo")
    print("8. Salir")



def limpiar_pantalla():
    time.sleep(2)
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    global agenda
    agenda = []
    global system
    if os.name == "nt":
        system = "Windows"
    else:
        system = "Linux"
    menu()
    while True:
        opcion = input("Opcion: ")
        if opcion == "1":
            agregar_contacto()
            limpiar_pantalla()
        elif opcion == "2":
            ver_contactos()
            limpiar_pantalla()
        elif opcion == "3":
            buscar_contacto()
            limpiar_pantalla()
        elif opcion == "4":
            editar_contacto()
            limpiar_pantalla()
        elif opcion == "5":
            eliminar_contacto()
            limpiar_pantalla()
        elif opcion == "6":
            cargar_contactos()
            limpiar_pantalla()
        elif opcion == "7":
            guardar_contactos()
            limpiar_pantalla()
        elif opcion == "8":
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()
