def modus_ponens():
    # Explicación sobre las premisas y el funcionamiento del programa
    print("Este programa implementa el Modus Ponens, un principio de lógica que se utiliza para inferir una consecuencia a partir de una condición.")
    print("Por favor, ingrese las premisas en el siguiente formato:")
    print("Premisa mayor: 'Si [condición], entonces [consecuencia]'")
    print("Premisa menor: '[condición]'")
    print("Por ejemplo, si la premisa mayor es 'Si llueve, entonces las calles estarán mojadas', y la premisa menor es 'Está lloviendo', el programa inferirá 'Las calles estarán mojadas'.")
    print()

    # Solicitar al usuario ingresar las premisas
    premisa_mayor = input("Ingrese la premisa mayor: ")
    premisa_menor = input("Ingrese la premisa menor: ")

    # Analizar las premisas
    premisa_mayor = premisa_mayor.strip().split(",")
    premisa_menor = premisa_menor.strip()

    # Verificar si las premisas tienen el formato correcto
    if len(premisa_mayor) != 2:
        return "Por favor, ingrese la premisa mayor en el formato correcto."

    # Extraer la condición y la consecuencia de la premisa mayor
    condicion = premisa_mayor[0].strip()
    consecuencia = premisa_mayor[1] # Obtener la última palabra (la consecuencia)

    # Verificar si la premisa menor coincide con la condición de la premisa mayor
    if premisa_menor != condicion:
        return f"La premisa menor no coincide con la condición de la premisa mayor ('{condicion}')."

    # Imprimir la conclusión
    return f"Por lo tanto, '{consecuencia}'."

# Ejecutar el programa interactivo
print(modus_ponens())