# Nombre del archivo donde se guardará la información
archivo_informacion = "informacion_bot.txt"

# Función para cargar la información del archivo
def cargar_informacion():
    try:
        with open(archivo_informacion, "r") as archivo:
            return eval(archivo.read())  # Cargar como diccionario
    except FileNotFoundError:
        return {}

# Función para guardar la información en el archivo
def guardar_informacion(informacion):
    with open(archivo_informacion, "w") as archivo:
        archivo.write(str(informacion))

# Función privada para eliminar un tema
def _eliminar_tema(informacion_bot, tema):
    if tema in informacion_bot:
        del informacion_bot[tema]
        print("Sung Jin-Woo: El tema '{}' ha sido eliminado.".format(tema))
        guardar_informacion(informacion_bot)
    else:
        print("Sung Jin-Woo: No se encontró el tema '{}'.".format(tema))

# Mensajes amigables para el usuario
mensaje_saludo = "¡Hola! Soy Sung Jin-Woo, tu asistente personal. ¿Cómo estás?"
pregunta_tema = "¿De qué tema te gustaría aprender o enseñarme el día de hoy? :)"
mensaje_despedida = "¡Hasta luego! Que tengas un excelente día."

# Función para manejar las interacciones del usuario con el bot
def chat():
    informacion_bot = cargar_informacion()
    print(mensaje_saludo)
    estado_usuario = input("Usuario: ")
    informacion_bot["Estado del usuario"] = estado_usuario
    while True:
        opcion = input("Por favor, selecciona una opción:\n1. Ver temas disponibles\n2. Hablar sobre un tema\n3. Eliminar tema (Requiere contraseña)\n4. Salir\nOpción: ")
        if opcion == "1":
            temas_disponibles = list(informacion_bot.keys())
            temas_disponibles.remove("Estado del usuario")  # Eliminar estado del usuario de la lista de temas
            temas_disponibles.remove("Último mensaje")  # Eliminar último mensaje de la lista de temas
            print("Temas disponibles:")
            for tema in temas_disponibles:
                print("-", tema)
        elif opcion == "2":
            tema = input(pregunta_tema + "\nUsuario: ")
            if tema in informacion_bot:
                print("Sung Jin-Woo:", informacion_bot[tema])
            else:
                respuesta = input(f"Sung Jin-Woo: Lo siento, no tengo información sobre '{tema}'. ¿Te gustaría agregar información sobre este tema? (si/no): ")
                if respuesta.lower() == "si":
                    nueva_informacion = input(f"Sung Jin-Woo: Por favor, ingresa información sobre '{tema}': ")
                    informacion_bot[tema] = nueva_informacion
                    print("Sung Jin-Woo: ¡Entendido! La información ha sido agregada.")
                    guardar_informacion(informacion_bot)
                else:
                    print("Sung Jin-Woo: De acuerdo, si necesitas información sobre otro tema, solo pregúntame.")
        elif opcion == "3":
            contraseña = input("Por favor, ingresa la contraseña para eliminar un tema: ")
            if contraseña == "1234":
                print("Temas disponibles:")
                for tema in informacion_bot.keys():
                    if tema not in ["Estado del usuario", "Último mensaje"]:
                        print("-", tema)
                tema_eliminar = input("Por favor, ingresa el nombre del tema que deseas eliminar: ")
                if tema_eliminar in informacion_bot:
                    confirmacion = input(f"¿Estás seguro de eliminar el tema '{tema_eliminar}' y su contenido? (si/no): ")
                    if confirmacion.lower() == "si":
                        _eliminar_tema(informacion_bot, tema_eliminar)
                else:
                    print("Sung Jin-Woo: No se encontró el tema '{}'.".format(tema_eliminar))
            else:
                print("Sung Jin-Woo: Contraseña incorrecta. No tienes permiso para eliminar temas.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
    print("Sung Jin-Woo:", mensaje_despedida)
    informacion_bot["Último mensaje"] = mensaje_despedida
    guardar_informacion(informacion_bot)

# Ejecutar el chat
if __name__ == "__main__":
    chat()