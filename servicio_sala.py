# Nombre del estudiante: Carlos Daniel Marin Amaris
# Grupo: 213023
# Programa: Ingenieria de Sistemas
# Curso: Programacion
# Centro: CEAD Valledupar
# Codigo fuente: autoria propia

from servicio import Servicio

class ServicioSala(Servicio):
    """Representa el servicio de alquiler de salas."""

    TIPO_SERVICIO = "Sala" # Constante de clase que indica el tipo de servicio. Esto permite identificar fácilmente el tipo de servicio sin necesidad de instanciar un objeto.

    def __init__(self, identificador, nombre, descripcion, tarifa_por_hora, estado=True):
        super().__init__(identificador, nombre, descripcion, estado)

        self.tarifa_por_hora = tarifa_por_hora  # Tarifa por hora para el alquiler de la sala

    @property
    def tarifa_por_hora(self):
        return self._tarifa_por_hora

    @tarifa_por_hora.setter
    def tarifa_por_hora(self, nueva_tarifa):
        self._tarifa_por_hora = self._validar_tarifa(nueva_tarifa)


    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo del servicio."""
        duracion = self._validar_duracion(duracion)

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool): 
            raise TypeError("El impuesto debe ser un valor númerico.")
        if impuesto < 0 or impuesto > 100:
            raise ValueError("El impuesto debe ser un valor númerico entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool):
            raise TypeError("El descuento debe ser un valor númerico.")
        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe ser un valor númerico entre 0 y 100.")
        impuesto /= 100   # Convertir el porcentaje a decimal
        descuento /= 100  
        
        costo_base = duracion * self.tarifa_por_hora
        costo_con_impuesto = costo_base + (costo_base * impuesto)
        costo_final = costo_con_impuesto - (costo_con_impuesto * descuento)
        return costo_final

    def describir_servicio(self):
        """Devuelve una descripción detallada del servicio de alquiler de salas."""
        return (f"=== SERVICIO DE ALQUILER DE SALAS ===\n"
                f"Servicio       : {self.nombre}\n"
                f"ID Sala        : {self.identificador}\n"
                f"Descripción    : {self.descripcion}\n"
                f"Tarifa por hora: ${self.tarifa_por_hora:.0f}\n"
                f"Estado         : {'Disponible' if self.estado else 'No disponible'}")

    def validar_parametros(self):
        """
        Valida que los parámetros específicos del servicio sean correctos.
        """

        self._validar_tarifa(self.tarifa_por_hora)

        return True
    