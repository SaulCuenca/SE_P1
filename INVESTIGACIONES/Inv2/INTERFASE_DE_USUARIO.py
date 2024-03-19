# Base de conocimiento inicial
base_conocimiento = {
    "preguntas": {
        "1": "¿Cómo te sientes hoy? (feliz/triste/enojado)",
        "2": "¿Has tenido algún problema recientemente? (si/no)",
        "3": "¿Tienes dificultades para concentrarte en tus tareas? (si/no)",
        "4": "¿Tienes problemas para dormir? (si/no)"
    },
    "reglas": {
        "feliz": {"1": "feliz", "2": "no", "3": "no", "4": "no"},
        "triste": {"1": "triste", "2": "si", "3": "si", "4": "si"},
        "enojado": {"1": "enojado", "2": "si", "3": "si", "4": "si"}
    }
}

# Función para realizar inferencia en el sistema experto
def motor_inferencia(respuestas):
    emociones = []
    for emocion, regla in base_conocimiento["reglas"].items():
        if all(respuestas[num_pregunta] == respuesta for num_pregunta, respuesta in regla.items()):
            emociones.append(emocion)
    return emociones

# Función principal para interactuar con el usuario
def interfaz_usuario():
    print("¡Bienvenido a la Interfaz de Usuario del Sistema Experto!")
    respuestas = {}
    for num_pregunta, pregunta in base_conocimiento["preguntas"].items():
        respuesta = input(pregunta + " ")
        respuestas[num_pregunta] = respuesta.lower()
    resultado = motor_inferencia(respuestas)
    if resultado:
        print("\nBasado en tus respuestas, podrías estar sintiéndote:")
        for emocion in resultado:
            print(emocion)
    else:
        print("\nNo se pudo determinar tu estado emocional con las respuestas proporcionadas.")

# Ejecutar la interfaz de usuario
interfaz_usuario()