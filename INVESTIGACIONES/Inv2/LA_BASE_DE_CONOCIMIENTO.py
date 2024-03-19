# Definir la base de conocimiento como un diccionario
base_conocimiento = {
    "enfermedades": {
        "resfriado": {
            "sintomas": ["fiebre leve", "tos", "congestión nasal"],
            "tratamiento": "Descansar, beber líquidos y tomar medicamentos para la fiebre y la congestión."
        },
        "gripe": {
            "sintomas": ["fiebre alta", "dolor muscular", "fatiga"],
            "tratamiento": "Descansar, beber líquidos, tomar medicamentos para la fiebre y el dolor, y vacunarse contra la gripe."
        },
        "COVID-19": {
            "sintomas": ["fiebre", "tos seca", "dificultad para respirar"],
            "tratamiento": "Aislamiento, reposo, hidratación y tratamiento sintomático. Consultar a un médico si los síntomas empeoran."
        }
    },
    "alergias": {
        "polen": ["estornudos", "picazón en los ojos", "congestión nasal"],
        "alimentos": ["urticaria", "hinchazón de labios", "dolor abdominal"]
    }
}

# Función para buscar información en la base de conocimiento
def buscar_informacion(enfermedad):
    # Convertir la entrada a minúsculas para facilitar la comparación
    enfermedad = enfermedad.lower()
    
    if enfermedad in base_conocimiento["enfermedades"]:
        info = base_conocimiento["enfermedades"][enfermedad]
        print(f"Aquí tienes información sobre {enfermedad}:")
        print("Síntomas:", ", ".join(info["sintomas"]))
        print("Tratamiento:", info["tratamiento"])
    else:
        print("Lo siento, no tenemos información sobre esa enfermedad en nuestra base de conocimiento.")

# Mensaje de bienvenida al usuario
print("¡Hola! Soy tu asistente de salud personal.")
print("Puedo proporcionarte información sobre diferentes enfermedades y alergias.")
print("Por favor, ingresa el nombre de la enfermedad que te interese.")

# Solicitar al usuario el nombre de la enfermedad
enfermedad = input("Enfermedad: ")
# Llamar a la función para buscar información
buscar_informacion(enfermedad)