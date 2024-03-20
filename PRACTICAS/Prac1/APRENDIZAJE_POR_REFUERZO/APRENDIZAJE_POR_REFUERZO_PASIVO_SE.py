import random

# Clase que representa el sistema experto de recomendación de actividad
class SistemaRecomendacion:
    def __init__(self):
        # Base de conocimientos con las actividades y sus recompensas
        self.base_conocimientos = {
            "leer": 0,
            "caminar": 0,
            "ver una película": 0,
            "cocinar una nueva receta": 0
        }

    def seleccionar_actividad(self):
        # Selección de actividad basada en las preferencias aprendidas
        return max(self.base_conocimientos, key=self.base_conocimientos.get)

    def recibir_refuerzo_pasivo(self, actividad):
        # Simulación de refuerzo pasivo: aumenta la recompensa de la actividad recibida
        self.base_conocimientos[actividad] += 1

# Función principal del sistema
def sistema_experto():
    sistema = SistemaRecomendacion()

    # Simulación de refuerzo pasivo durante un período de tiempo
    for _ in range(100):
        actividad_seleccionada = random.choice(list(sistema.base_conocimientos.keys()))
        sistema.recibir_refuerzo_pasivo(actividad_seleccionada)

    # Selección de la actividad con mayor recompensa
    actividad_recomendada = sistema.seleccionar_actividad()

    print("Sistema: Basado en refuerzo pasivo, te recomiendo hacer:", actividad_recomendada)

# Ejecutar el sistema
if __name__ == "__main__":
    sistema_experto()