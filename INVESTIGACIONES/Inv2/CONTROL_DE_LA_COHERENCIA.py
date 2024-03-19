# Definir una base de conocimiento inicial
base_conocimiento = {
    "enfermedades": {
        "resfriado": ["fiebre leve", "tos", "congestión nasal"],
        "gripe": ["fiebre alta", "dolor muscular", "fatiga"],
        "COVID-19": ["fiebre", "tos seca", "dificultad para respirar"]
    },
    "alergias": {
        "polen": ["estornudos", "picazón en los ojos", "congestión nasal"],
        "gripe": ["fiebre alta", "dolor muscular", "fatiga"],
        "alimentos": ["urticaria", "hinchazón de labios", "dolor abdominal"]
    }
}

# Función para verificar la coherencia de la base de conocimiento
def verificar_coherencia():
    enfermedades = set()
    for categoria, elementos in base_conocimiento.items():
        for nombre, atributos in elementos.items():
            # Verificar si hay elementos duplicados dentro de cada categoría
            if nombre in enfermedades:
                print(f"Advertencia: La enfermedad '{nombre}' está duplicada en la categoría '{categoria}'.")
                print("¿Qué te gustaría hacer?")
                print("1. Eliminar la enfermedad duplicada.")
                print("2. Modificar los atributos de la enfermedad.")
                opcion = input("Por favor, ingresa el número de la opción que deseas realizar (1/2): ")
                if opcion == "1":
                    del base_conocimiento[categoria][nombre]
                    print(f"La enfermedad '{nombre}' ha sido eliminada.")
                elif opcion == "2":
                    print(f"Los atributos actuales de la enfermedad '{nombre}' son: {', '.join(atributos)}")
                    nuevos_atributos = input("Por favor, ingresa los nuevos atributos (separados por coma): ").split(',')
                    base_conocimiento[categoria][nombre] = nuevos_atributos
                    print(f"Los atributos de la enfermedad '{nombre}' han sido modificados.")
                else:
                    print("Opción no válida. Volviendo al menú principal.")
            else:
                enfermedades.add(nombre)

# Ejecutar la función de verificación de coherencia
verificar_coherencia()