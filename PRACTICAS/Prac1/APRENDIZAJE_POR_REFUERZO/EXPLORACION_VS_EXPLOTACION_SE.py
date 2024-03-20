import random

# Clase que representa el sistema experto para recomendación de restaurantes
class RecomendadorRestaurantes:
    def __init__(self):
        # Base de datos de restaurantes con sus calificaciones
        self.restaurantes = {
            "Restaurante BRICK STEAKHOUSE": 4.5,
            "Restaurante MARISCOS ALEX": 4.0,
            "Restaurante KFC": 3.8,
            "Restaurante CAMPO MAR": 4.2,
            "Restaurante MCDONALDS": 3.9
        }

    def recomendar_restaurante(self, estrategia):
        if estrategia == "exploracion":
            # Exploración: seleccionar un restaurante aleatorio
            return random.choice(list(self.restaurantes.keys()))
        elif estrategia == "explotacion":
            # Explotación: seleccionar el restaurante mejor calificado
            return max(self.restaurantes, key=self.restaurantes.get)

# Función principal del programa
def exploracion_vs_explotacion():
    recomendador = RecomendadorRestaurantes()

    print("¡Bienvenido al recomendador de restaurantes!")
    estrategia = input("¿Qué estrategia deseas utilizar? (exploracion/explotacion): ").lower()

    if estrategia not in ["exploracion", "explotacion"]:
        print("Estrategia no válida. Seleccionando exploración por defecto.")
        estrategia = "exploracion"

    restaurante_recomendado = recomendador.recomendar_restaurante(estrategia)
    print("Te recomiendo visitar el restaurante:", restaurante_recomendado)

# Ejecutar el programa
if __name__ == "__main__":
    exploracion_vs_explotacion()