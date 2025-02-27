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



def ver_contactos():
    print("Ver contactos")
    for contacto in agenda:
        print("ID: ", contacto["id"])
        print("Nombre: ", contacto["nombre"])
        print("Telefono: ", contacto["telefono"])
        print("Email: ", contacto["email"])
        print("---------------")

def buscar_contacto():
  contacto["email"])
                print("---------------")
                encontrado = True
        if not encontrado:
            print("Contacto no encontrado")
    elif opcion == "2":
        telefono = input("Telefono: ")
        for contacto in agenda:
            if contacto["telefono"] == telefono:
                print("ID: ", contacto["id"])
                print("Nombre: ", contacto["nombre"])
                print("Telefono: ", contacto["telefono"])
                print("Email: ", contacto["email"])
                print("---------------")
                encontrado = True
        if not encontrado:
            print("Contacto no encontrado")
    elif opcion == "3":
        email = input("Email: ")
        for contacto in agenda:
            if contacto["email"] == email:
                print("ID: ", contacto["id"])
                print("Nombre: ", contacto["nombre"])
                print("Telefono: ", contacto["telefono"])
                print("Email: ", contacto["email"])
                print("---------------")
                encontrado = True
        if not encontrado:
            print("Contacto no encontrado")
    else:
        print("Opcion no valida")

def editar_contacto():
    ver_contactos()
    id = int(input("ID del contacto a editar: "))

    for contacto in agenda:
        if contacto["id"] == id:
            encontrado = True
            print("1. Nombre")
            print("2. Telefono")
            print("3. Email")
            opcion = input("Opcion: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                contacto["nombre"] = nombre
            elif opcion == "2":
                telefono = input("Telefono: ")
                contacto["telefono"] = telefono
            elif opcion == "3":
                email = input("Email: ")
                contacto["email"] = email
            else:
                print("Opcion no valida")
            print("Contacto editado")
            break
    if not encontrado:
        print("Contacto no encontrado")



def guardar_contactos():
    with open("contactos.csv", "w") as archivo:
        for contacto in agenda:
            archivo.write(f"{contacto['nombre']},{contacto['telefono']},{contacto['email']}\n")

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