import random

# Clase que representa el sistema experto para la búsqueda de política
class PlanificadorRutas:
    def __init__(self):
        self.mapa = {
            "calle1": ["calle2", "calle3"],
            "calle2": ["calle1", "calle4"],
            "calle3": ["calle1", "calle4"],
            "calle4": ["calle2", "calle3", "calle5"],
            "calle5": ["calle4", "calle6"],
            "calle6": ["calle5", "calle7"],
            "calle7": ["calle6"]
        }

    def seleccionar_accion(self, estado):
        # Selecciona una acción aleatoria de las posibles para el estado actual
        return random.choice(self.mapa[estado])

# Función principal del programa
def planificar_ruta():
    planificador = PlanificadorRutas()
    estado_actual = "calle1"  # Estado inicial

    print("¡Bienvenido al planificador de rutas hacia tu casa!")
    print("Tu casa se encuentra en la 'calle7'.")

    while estado_actual != "calle7":
        print("Te encuentras en la", estado_actual)
        print("¿Qué camino tomarás?")
        print("Opciones:", ", ".join(planificador.mapa[estado_actual]))
        proximo_paso = input("Ingresa el nombre de la calle a la que te dirigirás: ")

        if proximo_paso in planificador.mapa[estado_actual]:
            estado_actual = proximo_paso
        else:
            print("¡Camino no válido! Por favor, elige una de las opciones disponibles.")

    print("¡Felicidades! Has llegado a tu casa.")

# Ejecutar el planificador de rutas
if __name__ == "__main__":
    planificar_ruta()