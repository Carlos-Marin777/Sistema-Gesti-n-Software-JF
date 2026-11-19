# Nombre del estudiante: Carlos Daniel Marin Amaris
# Grupo: 213023
# Programa: Ingenieria de Sistemas
# Curso: Programacion
# Centro: CEAD Valledupar
# Codigo fuente: autoria propia


from recurso import Recurso


class Sala(Recurso):
    """Representa un recurso de sala."""

    TIPO_SERVICIO = "Sala"  # Constante de clase que indica el tipo de servicio. Esto permite identificar fácilmente el tipo de servicio sin necesidad de instanciar un objeto.

    def __init__(self, identificador, nombre, capacidad, estado=True):
        super().__init__(identificador, nombre, estado)
        self.capacidad = capacidad  # Capacidad de la sala

    @property
    def capacidad(self):
        return self._capacidad

    def _validar_capacidad(self, capacidad):
        """Valida que la capacidad de la sala sea un número entero positivo."""
        if not isinstance(capacidad, int) or isinstance(capacidad, bool):
            raise TypeError("La capacidad debe ser un número entero positivo.")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo.")
        return capacidad

    @capacidad.setter
    def capacidad(self, nueva_capacidad):
        self._capacidad = self._validar_capacidad(nueva_capacidad)

    def describir_recurso(self):
        """Devuelve una descripción detallada del recurso de sala."""
        return (f"=== RECURSO DE SALA ===\n"
                f"Recurso  : {self.nombre}\n"
                f"ID       : {self.identificador}\n"
                f"Capacidad: {self.capacidad} personas\n"
                f"Estado   : {'Disponible' if self.estado else 'No disponible'}")

    def validar_parametros(self):
        """Valida que los parámetros específicos del recurso sean correctos."""
        self._validar_capacidad(self.capacidad)
        return True