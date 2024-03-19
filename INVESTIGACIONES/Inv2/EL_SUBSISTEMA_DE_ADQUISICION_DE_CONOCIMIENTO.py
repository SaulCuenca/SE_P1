# Base de conocimiento inicial
base_conocimiento = {
    "reglas": [
        {"si": ["fiebre"], "entonces": "resfriado"},
        {"si": ["fiebre alta", "dolor muscular"], "entonces": "gripe"},
        {"si": ["fiebre", "tos seca", "dificultad para respirar"], "entonces": "COVID-19"},
        {"si": ["estornudos", "picazón en los ojos", "congestión nasal"], "entonces": "alergia al polen"},
        {"si": ["urticaria", "hinchazón de labios", "dolor abdominal"], "entonces": "alergia a alimentos"}
    ]
}

# Función para mostrar la base de conocimiento actual
def mostrar_base_conocimiento():
    print("----- Base de Conocimiento -----")
    for idx, regla in enumerate(base_conocimiento["reglas"], start=1):
        print(f"{idx}. Si {', '.join(regla['si'])}, entonces {regla['entonces']}")

# Función para agregar una nueva regla a la base de conocimiento
def agregar_regla():
    print("\nAgregando una nueva regla a la base de conocimiento:")
    condicion = input("Ingresa las condiciones separadas por coma (por ejemplo, fiebre, tos): ").split(',')
    conclusion = input("Ingresa la conclusión: ")
    base_conocimiento["reglas"].append({"si": [sintoma.strip() for sintoma in condicion], "entonces": conclusion})
    print("Nueva regla agregada con éxito.")

# Función principal para interactuar con el usuario
def main():
    print("¡Bienvenido al Subsistema de Adquisición de Conocimiento!")
    while True:
        mostrar_base_conocimiento()
        print("\n¿Qué te gustaría hacer?")
        print("1. Agregar nueva regla")
        print("2. Salir")
        opcion = input("Por favor, ingresa el número de la opción que deseas realizar: ")
        if opcion == "1":
            agregar_regla()
        elif opcion == "2":
            print("Saliendo del Subsistema de Adquisición de Conocimiento.")
            break
        else:
            print("Opción no válida. Por favor, ingresa una opción válida.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()