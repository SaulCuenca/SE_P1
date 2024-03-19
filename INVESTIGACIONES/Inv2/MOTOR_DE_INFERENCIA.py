# Definir una base de conocimiento con reglas
base_conocimiento = {
    "reglas": [
        {"si": ["fiebre"], "entonces": "resfriado"},
        {"si": ["fiebre alta", "dolor muscular"], "entonces": "gripe"},
        {"si": ["fiebre", "tos seca", "dificultad para respirar"], "entonces": "COVID-19"},
        {"si": ["estornudos", "picazón en los ojos", "congestión nasal"], "entonces": "alergia al polen"},
        {"si": ["urticaria", "hinchazón de labios", "dolor abdominal"], "entonces": "alergia a alimentos"}
    ]
}

# Función para realizar inferencia en el sistema experto
def motor_inferencia(sintomas):
    enfermedades = []
    for regla in base_conocimiento["reglas"]:
        if all(sintoma in sintomas for sintoma in regla["si"]):
            enfermedades.append(regla["entonces"])
    return enfermedades

# Función principal para interactuar con el usuario
def main():
    print("¡Bienvenido al Motor de Inferencia!")
    print("Ingresa los síntomas que experimenta el paciente separados por coma (por ejemplo, fiebre, tos, dolor muscular):")
    sintomas_input = input()
    sintomas = [sintoma.strip() for sintoma in sintomas_input.split(',')]
    resultado = motor_inferencia(sintomas)
    if resultado:
        print("Basado en los síntomas proporcionados, el paciente podría tener las siguientes enfermedades:")
        for enfermedad in resultado:
            print(enfermedad)
    else:
        print("No se encontraron enfermedades basadas en los síntomas proporcionados.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()