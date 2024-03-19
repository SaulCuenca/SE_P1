# Base de conocimiento inicial
base_conocimiento = {
    "reglas": [
        {"si": ["fiebre"], "entonces": "Tomar paracetamol"},
        {"si": ["dolor muscular"], "entonces": "Tomar ibuprofeno"},
        {"si": ["tos seca", "dificultad para respirar"], "entonces": "Consultar a un médico"}
    ]
}

# Función para explicar la decisión basada en las reglas
def explicar_decision(sintomas, decisiones):
    explicaciones = []
    for sintoma in sintomas:
        explicaciones.append(f"El paciente presenta el síntoma: {sintoma}")
    for decision in decisiones:
        explicaciones.append(f"Se recomienda: {decision}")
    return explicaciones

# Función principal para interactuar con el usuario
def main():
    print("¡Bienvenido al Subsistema de Explicación!")
    print("Por favor, ingresa los síntomas que experimenta el paciente (separados por coma):")
    sintomas_input = input()
    sintomas = [sintoma.strip() for sintoma in sintomas_input.split(',')]
    decisiones = []
    for regla in base_conocimiento["reglas"]:
        if all(sintoma in sintomas for sintoma in regla["si"]):
            decisiones.append(regla["entonces"])
    if decisiones:
        explicaciones = explicar_decision(sintomas, decisiones)
        print("\nExplicación:")
        for explicacion in explicaciones:
            print(explicacion)
    else:
        print("\nNo hay recomendaciones basadas en los síntomas proporcionados.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()