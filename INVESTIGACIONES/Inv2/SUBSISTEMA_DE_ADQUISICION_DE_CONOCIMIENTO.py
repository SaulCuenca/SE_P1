# Definir una base de conocimiento inicial vacía
base_conocimiento = {}

# Función para agregar nuevo conocimiento a la base de conocimiento
def agregar_conocimiento():
    print("Por favor, ingresa la nueva información:")
    categoria = input("Categoría (por ejemplo, enfermedades, síntomas, tratamientos): ").lower()
    nombre = input("Nombre: ").lower()
    atributos = input("Atributos (separados por coma): ").split(',')
    
    # Verificar si la categoría ya existe en la base de conocimiento
    if categoria not in base_conocimiento:
        base_conocimiento[categoria] = {}
    
    # Agregar la nueva información a la base de conocimiento
    base_conocimiento[categoria][nombre] = atributos
    
    print("¡Nueva información agregada con éxito!")

# Función para revisar la información en la base de conocimiento
def revisar_conocimiento():
    print("\n--- Información en la base de conocimiento ---")
    for categoria, elementos in base_conocimiento.items():
        print(f"\nCategoría: {categoria.capitalize()}")
        for nombre, atributos in elementos.items():
            print(f"Nombre: {nombre.capitalize()}")
            print("Atributos:", ", ".join(atributos))

# Función principal para interactuar con el usuario
def main():
    print("¡Bienvenido al Subsistema de Adquisición de Conocimiento!")
    print("Este programa te permite agregar nueva información a la base de conocimiento.")
    
    # Solicitar al usuario si desea agregar o revisar información
    while True:
        accion = input("\n¿Qué acción deseas realizar? (agregar/revisar/salir): ").lower()
        if accion == "agregar":
            agregar_conocimiento()
        elif accion == "revisar":
            revisar_conocimiento()
        elif accion == "salir":
            print("Gracias por usar el Subsistema de Adquisición de Conocimiento. ¡Hasta luego!")
            break
        else:
            print("Por favor, selecciona una acción válida.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
