# Definición de la base de conocimiento con algunas reglas de ejemplo
base_conocimiento = {
    "reglas": [
        {"si": ["fiebre"], "entonces": "Tomar paracetamol"},
        {"si": ["dolor muscular"], "entonces": "Tomar ibuprofeno"},
        {"si": ["tos seca", "dificultad para respirar"], "entonces": "Consultar a un médico"}
    ]
}

# Función para ejecutar las órdenes basadas en el conocimiento
def ejecutar_ordenes(sintomas):
    acciones = []
    for regla in base_conocimiento["reglas"]:
        if all(sintoma in sintomas for sintoma in regla["si"]):
            acciones.append(regla["entonces"])
    return acciones

# Función principal para interactuar con el usuario
def main():
    print("¡Bienvenido al Subsistema de Ejecución de Órdenes!")
    print("Por favor, ingresa los síntomas que experimenta el paciente (separados por coma):")
    sintomas_input = input()
    sintomas = [sintoma.strip() for sintoma in sintomas_input.split(',')]
    acciones = ejecutar_ordenes(sintomas)
    if acciones:
        print("\nBasado en los síntomas proporcionados, se recomienda lo siguiente:")
        for accion in acciones:
            print("- " + accion)
    else:
        print("\nNo se encontraron recomendaciones para los síntomas proporcionados.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()