import heapq

class Tarea:
    def __init__(self, prioridad, descripcion):
        self.prioridad = prioridad
        self.descripcion = descripcion

    def __lt__(self, other):
        # Esto permite comparar tareas por prioridad automáticamente en el heap
        return self.prioridad < other.prioridad

    def __repr__(self):
        return f"{self.descripcion} (prioridad: {self.prioridad})"

class GestorDeTareas:
    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, tarea):
        heapq.heappush(self._tareas, tarea)

    def obtener_tarea_mas_prioritaria(self):
        if self._tareas:
            return heapq.heappop(self._tareas)
        return None

    def mostrar_todas(self):
        return sorted(self._tareas)

# Ejemplo de uso
gestor = GestorDeTareas()
gestor.agregar_tarea(Tarea(2, 'Hacer compras'))
gestor.agregar_tarea(Tarea(1, 'Estudiar Python'))
gestor.agregar_tarea(Tarea(3, 'Llamar a mamá'))

print("Tareas en orden de prioridad:")
while True:
    tarea = gestor.obtener_tarea_mas_prioritaria()
    if tarea is None:
        break
    print(tarea)
