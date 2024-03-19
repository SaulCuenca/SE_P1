# Base de conocimiento inicial
base_conocimiento = []

# Función para aprender nuevas reglas y actualizar la base de conocimiento
def aprender_nuevas_reglas(ejemplos):
    for entrada, salida in ejemplos:
        base_conocimiento.append({"entrada": entrada, "salida": salida})

# Función para mostrar todas las reglas en la base de conocimiento
def mostrar_reglas():
    print("Las reglas actuales en la base de conocimiento son:")
    for idx, regla in enumerate(base_conocimiento, 1):
        print(f"Regla {idx}: Si la entrada es {regla['entrada']}, entonces la salida es {regla['salida']}")

# Función principal para interactuar con el usuario
def main():
    while True:
        print("\n¡Bienvenido al Subsistema de Aprendizaje!")
        print("Por favor, seleccione una opción:")
        print("1. Mostrar reglas actuales")
        print("2. Aprender nueva regla")
        print("3. Salir")
        opcion = input("Ingrese el número de la opción seleccionada: ")

        if opcion == "1":
            mostrar_reglas()
        elif opcion == "2":
            print("Por favor, ingrese un nuevo ejemplo de entrada y salida:")
            entrada = input("Ingrese la entrada: ")
            salida = input("Ingrese la salida correspondiente: ")
            aprender_nuevas_reglas([(entrada, salida)])
            print("\nEl nuevo ejemplo ha sido aprendido y agregado a la base de conocimiento.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1, 2 o 3).")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
