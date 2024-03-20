import random

# Clase que representa el sistema experto de recomendación de comida
class SistemaRecomendacion:
    def __init__(self):
        # Base de conocimientos con las preferencias de comida y recompensas
        self.base_conocimientos = {
            "pasta": 0,
            "pizza": 0,
            "ensalada": 0
        }

    def seleccionar_comida(self):
        # Selección de comida basada en las preferencias aprendidas
        return max(self.base_conocimientos, key=self.base_conocimientos.get)

    def actualizar_preferencia(self, comida, recompensa):
        # Actualización de las preferencias basada en la retroalimentación de la comida seleccionada
        self.base_conocimientos[comida] += recompensa



# Función principal del sistema
def sistema_experto():
    print("¡Hola! Soy tu asistente de recomendación de comida. ¿Qué te gustaría comer hoy?")
    print("Por favor, proporcióname tu opinión después de cada recomendación.")

    sistema = SistemaRecomendacion()

    # Simulación de interacciones del usuario
    for _ in range(3):
        comida_sugerida = sistema.seleccionar_comida()
        print("Sistema: Te recomiendo pedir", comida_sugerida)
        retroalimentacion = input("¿Te gustó la recomendación? (sí/no): ")
        if retroalimentacion.lower() == "si":
            sistema.actualizar_preferencia(comida_sugerida, 1)  # Recompensa positiva
        else:
            sistema.actualizar_preferencia(comida_sugerida, -1)  # Recompensa negativa

    print("Sistema: Gracias por tus comentarios. Basado en eso, aquí está mi recomendación final:")
    print("Sistema: Deberías pedir", sistema.seleccionar_comida())

# Ejecutar el sistema
if __name__ == "__main__":
    sistema_experto()