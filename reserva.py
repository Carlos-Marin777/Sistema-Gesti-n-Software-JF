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


from cliente import Cliente
from servicio import Servicio
from recurso import Recurso
from datetime import datetime
from logger import Logger
from excepciones import (
    RecursoNoDisponibleError,
    ReservaYaConfirmadaError,
    ReservaYaCanceladaError,
    ReservaYaFinalizadaError,
    ServicioNoDisponibleError,
    FormatoHoraInvalidoError,
    FormatoFechaInvalidoError)


class Reserva:
    """Representa una reserva realizada por un cliente para un servicio específico."""
    ESTADOS_VALIDOS = (
        "Pendiente",
        "Confirmada",
        "Cancelada",
        "Finalizada"
    )

    def __init__(self, identificador, cliente, servicio, recurso, fecha, hora_inicio, duracion, estado="Pendiente" ):

        # Validar que el identificador sea una cadena de texto
        if not isinstance(identificador, str):
            raise TypeError("El identificador debe ser una cadena de texto.")
        identificador = identificador.strip().upper()  # Convertir a mayúsculas y eliminar espacios en blanco
        if not identificador:
            raise ValueError("El identificador de la reserva no puede estar vacío.")
        self._identificador = identificador
        
        self.cliente = cliente  
        self.servicio = servicio  
        self.recurso = recurso  
        self.fecha = fecha  
        self.hora_inicio = hora_inicio  
        self.duracion = duracion  
        self.estado = estado  

        self.costo_total = 0.0

    @property
    def identificador(self):
        return self._identificador

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, nuevo_cliente):
        if not isinstance(nuevo_cliente, Cliente):
            raise TypeError("El cliente debe ser una instancia de la clase Cliente.")
        self._cliente = nuevo_cliente


    @property
    def servicio(self):
        return self._servicio

    @servicio.setter
    def servicio(self, nuevo_servicio):
        if not isinstance(nuevo_servicio, Servicio):
            raise TypeError("El servicio debe ser una instancia de la clase Servicio.")
        self._servicio = nuevo_servicio


    @property
    def recurso(self):
        return self._recurso    

    @recurso.setter
    def recurso(self, nuevo_recurso):
        if not isinstance(nuevo_recurso, Recurso):
            raise TypeError("El recurso debe ser una instancia de la clase Recurso.")
        self._recurso = nuevo_recurso


    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        if not isinstance(nueva_fecha, str):
            raise TypeError("La fecha debe ser una cadena de texto con formato AAAA-MM-DD.")
        
        nueva_fecha = nueva_fecha.strip()

        if not nueva_fecha:
            raise ValueError("La fecha no puede estar vacía.")

        try:
            datetime.strptime(nueva_fecha, "%Y-%m-%d")
        except ValueError as error:
            raise FormatoFechaInvalidoError(
                "La fecha tiene un formato inválido. Debe ser AAAA-MM-DD."
            ) from error
        self._fecha = nueva_fecha


    @property
    def hora_inicio(self):
        return self._hora_inicio    

    @hora_inicio.setter
    def hora_inicio(self, nueva_hora_inicio):
        if not isinstance(nueva_hora_inicio, str):
            raise TypeError("La hora de inicio debe ser una cadena de texto con formato HH:MM.")

        nueva_hora_inicio = nueva_hora_inicio.strip()

        if not nueva_hora_inicio:
            raise ValueError("La hora de inicio no puede estar vacía.")

        try:
            datetime.strptime(nueva_hora_inicio, "%H:%M")
        except ValueError as error:
            raise FormatoHoraInvalidoError(
                "La hora de inicio tiene un formato inválido. Debe ser HH:MM."
            ) from error
        self._hora_inicio = nueva_hora_inicio

    @property
    def duracion(self):
        return self._duracion

    def _validar_duracion(self, duracion):
        """Método privado para validar la duración de la reserva. Se asegura de que la duración sea un número positivo."""
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise TypeError("La duración debe ser un número.")
        if duracion <= 0:
            raise ValueError("La duración debe ser un valor númerico positivo.")
        return duracion

    @duracion.setter
    def duracion(self, nueva_duracion):
        self._duracion = self._validar_duracion(nueva_duracion)


    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        if not isinstance(nuevo_estado, str):
            raise TypeError("El estado debe ser una cadena de texto.")

        nuevo_estado = nuevo_estado.strip().capitalize()

        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido. Los estados válidos son: {', '.join(self.ESTADOS_VALIDOS)}")
        self._estado = nuevo_estado    


    @property
    def costo_total(self):
        return self._costo_total

    @costo_total.setter
    def costo_total(self, nuevo_costo_total):
        if not isinstance(nuevo_costo_total, (int, float)) or isinstance(nuevo_costo_total, bool):
            raise TypeError("El costo total debe ser un valor númerico.")
        if nuevo_costo_total < 0:
            raise ValueError("El costo total no puede ser negativo.")
        self._costo_total =float(nuevo_costo_total)  


    def __str__(self):
        """Devuelve una representación legible de la reserva."""

        return (f"========== RESERVA ==========\n"
                f"ID Reserva    : {self.identificador}\n"
                f"Cliente       : {self.cliente.nombre}\n"
                f"Servicio      : {self.servicio.nombre}\n"
                f"Recurso       : {self.recurso.nombre}\n"
                f"Fecha         : {self.fecha}\n"
                f"Hora de inicio: {self.hora_inicio}\n"
                f"Duración      : {self.duracion} horas\n"
                f"Costo total   : ${self.costo_total:.2f}\n"
                f"Estado        : {self.estado}")


    def confirmar(self):
        """Confirma la reserva, cambiando su estado a 'Confirmada'."""
        if self.estado == "Confirmada":
            raise ReservaYaConfirmadaError("La reserva ya se encuentra confirmada.")
        if self.estado == "Cancelada":
            raise ReservaYaCanceladaError("No se puede confirmar una reserva cancelada.")
        if self.estado == "Finalizada":
            raise ReservaYaFinalizadaError("No se puede confirmar una reserva finalizada.")
        
        self.estado = "Confirmada"
        Logger.registrar(
            "INFO",
            f"Reserva confirmada: {self.identificador} | " 
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre}"
        )
                  

        return  True

    def cancelar(self):
        """Cancela la reserva, cambiando su estado a 'Cancelada'."""
        if self.estado == "Cancelada":
            raise ReservaYaCanceladaError("La reserva ya se encuentra cancelada.")
        if self.estado == "Finalizada":
            raise ReservaYaFinalizadaError("No se puede cancelar una reserva finalizada.")
        
        self.estado = "Cancelada"

        Logger.registrar(
            "INFO",
            f"Reserva cancelada: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre}"
            )
        
        return True


    def finalizar(self):
        """Finaliza la reserva cambiando su estado a 'Finalizada'."""

        if self.estado == "Finalizada":
            raise ReservaYaFinalizadaError(
                "La reserva ya se encuentra finalizada.")

        if self.estado == "Cancelada":
            raise ReservaYaCanceladaError(
                "No se puede finalizar una reserva cancelada.")

        self.estado = "Finalizada"

        Logger.registrar(
            "INFO",
            f"Reserva finalizada: {self.identificador} | "
        )

        return True


    def procesar(self, impuesto=0, descuento=0):
        """Procesa la reserva verificando disponibilidad, calculando el costo y confirmándola."""
        if not self.servicio.estado:
            raise ServicioNoDisponibleError("El servicio no está disponible.")
        if not self.recurso.estado:
            raise RecursoNoDisponibleError("El recurso no está disponible.")

        self.costo_total = self.servicio.calcular_costo(self.duracion, impuesto, descuento)

        self.confirmar()

        return True
    
