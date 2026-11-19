# Integrantes: 
# Carlos Daniel Marin Amaris
# Elian Rodriguez Buelvas
#
#
# Grupo: 213023
# Programa: Ingenieria de Sistemas
# Curso: Programacion
# Centro: CEAD Valledupar
# Codigo fuente: autoria propia



from recurso import Recurso

class Asesor(Recurso):
    """Representa un recurso de asesoría."""

    TIPO_SERVICIO = "Asesoria"  # Constante de clase que indica el tipo de servicio. Esto permite identificar fácilmente el tipo de servicio sin necesidad de instanciar un objeto.

    def __init__(self, identificador, nombre, especialidad, estado=True):
        super().__init__(identificador, nombre, estado)
        self.especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad
    

    def _validar_especialidad(self, especialidad):
        """Valida que la especialidad sea una cadena de texto no vacía."""

        if not isinstance(especialidad, str):
            raise TypeError("La especialidad debe ser una cadena de texto.")

        especialidad = especialidad.strip()
        if not especialidad:
            raise ValueError("La especialidad no puede estar vacía.")

        return especialidad.title()
    

    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        self._especialidad = self._validar_especialidad(nueva_especialidad)


    def describir_recurso(self):
        """Devuelve una descripción detallada del recurso de asesoría."""
        return (f"=== RECURSO DE ASESORÍA ===\n"
                f"Recurso     : {self.nombre}\n"
                f"ID          : {self.identificador}\n"
                f"Especialidad: {self.especialidad}\n"
                f"Estado      : {'Disponible' if self.estado else 'No disponible'}")
    

    def validar_parametros(self):
        """Valida que los parámetros específicos del recurso sean correctos."""
        self._validar_especialidad(self.especialidad)
        return True