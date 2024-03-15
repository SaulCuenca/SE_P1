def modus_tollens():
    # Explicación sobre las premisas y el funcionamiento del programa
    print("Este programa implementa el Modus Tollens, un principio de lógica que se utiliza para inferir la negación de una condición.")
    print("Por favor, ingrese las premisas en el siguiente formato:")
    print("Premisa mayor: 'Si [condición], entonces [consecuencia]'")
    print("Premisa menor: 'No [consecuencia]'")
    print("Por ejemplo, si la premisa mayor es 'Si hace sol, entonces las calles están secas', y la premisa menor es 'No las calles están secas', el programa inferirá 'No hace sol'.")
    print()

    # Solicitar al usuario ingresar las premisas
    premisa_mayor = input("Ingrese la premisa mayor: ")
    premisa_menor = input("Ingrese la premisa menor: ")

    # Analizar las premisas
    premisa_mayor = premisa_mayor.strip().split(",")
    premisa_menor = premisa_menor.strip().lower()

    # Verificar si las premisas tienen el formato correcto
    if len(premisa_mayor) != 2 or not premisa_menor.startswith("no "):
        return "Por favor, ingrese las premisas en el formato correcto."

    # Extraer la condición y la consecuencia de la premisa mayor
    condicion = premisa_mayor[0].strip()
    consecuencia = premisa_mayor[1].strip().split()[-1]  # Obtener la última palabra (la consecuencia)

    # Verificar si la premisa menor niega la consecuencia de la premisa mayor
    if premisa_menor[3:] != consecuencia:
        return "La premisa menor no niega la consecuencia de la premisa mayor."

    # Imprimir la conclusión
    return f"Por lo tanto, si '{condicion}' es falso."

# Ejecutar el programa interactivo
print(modus_tollens())