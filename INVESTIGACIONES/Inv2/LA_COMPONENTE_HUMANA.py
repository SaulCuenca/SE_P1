def sistema_experto():
    print("¡Bienvenido al Sistema Experto!")
    print("Por favor, responde las siguientes preguntas para recibir una orientación sobre tu salud.")

    # Solicitar información al usuario
    edad = int(input("¿Cuál es tu edad? "))
    sintomas = input("¿Experimentas fiebre, tos y dificultad para respirar? (responde si/no) ").lower()
    contacto_covid = input("¿Has estado en contacto con alguien diagnosticado con COVID-19? (responde si/no) ").lower()

    # Evaluar la situación basada en las respuestas del usuario
    if edad >= 60:
        if sintomas == "si":
            if contacto_covid == "si":
                print("Basado en tus respuestas, es posible que tengas COVID-19. Por favor, consulta a un médico lo antes posible.")
            else:
                print("Basado en tus respuestas, es posible que tengas gripe. Por favor, consulta a un médico si los síntomas empeoran.")
        else:
            print("Basado en tus respuestas, es posible que estés experimentando problemas de salud relacionados con la edad. Te recomendamos consultar a un médico para un diagnóstico preciso.")
    else:
        if sintomas == "si":
            print("Basado en tus respuestas, es posible que tengas un resfriado común. Descansa y mantente hidratado. Si los síntomas persisten, considera consultar a un médico.")
        else:
            print("Basado en tus respuestas, es menos probable que estés experimentando problemas graves de salud. Sin embargo, si los síntomas continúan o empeoran, te recomendamos buscar asesoramiento médico.")

# Ejecutar el sistema experto
sistema_experto()