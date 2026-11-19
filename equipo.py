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

class Equipo(Recurso):
    """Representa un recurso de equipo."""

    TIPO_SERVICIO = "Equipo"  # Constante de clase que indica el tipo de servicio. Esto permite identificar fácilmente el tipo de servicio sin necesidad de instanciar un objeto.

    def __init__(self, identificador, nombre, tipo_equipo, estado=True):
        super().__init__(identificador, nombre, estado)
        self.tipo_equipo = tipo_equipo
        

    @property
    def tipo_equipo(self):
        return self._tipo_equipo
    

    def _validar_tipo_equipo(self, tipo_equipo):
        """Valida que el tipo de equipo sea una cadena de texto no vacía."""

        if not isinstance(tipo_equipo, str):
            raise TypeError("El tipo de equipo debe ser una cadena de texto.")

        tipo_equipo = tipo_equipo.strip()
        if not tipo_equipo:
            raise ValueError("El tipo de equipo no puede estar vacío.")
        
        return tipo_equipo.title()
    

    @tipo_equipo.setter
    def tipo_equipo(self, nuevo_tipo):
        self._tipo_equipo = self._validar_tipo_equipo(nuevo_tipo)


    def describir_recurso(self):
        """Devuelve una descripción detallada del recurso de equipo."""
        return (f"=== RECURSO DE EQUIPO ===\n"
                f"Recurso       : {self.nombre}\n"
                f"ID            : {self.identificador}\n"
                f"Tipo de equipo: {self.tipo_equipo}\n"
                f"Estado        : {'Disponible' if self.estado else 'No disponible'}")
    

    def validar_parametros(self):
        """Valida que los parámetros específicos del recurso sean correctos."""
        self._validar_tipo_equipo(self.tipo_equipo)
        return True