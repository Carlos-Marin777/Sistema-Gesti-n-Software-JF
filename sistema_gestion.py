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
from reserva import Reserva
from logger import Logger
from excepciones import (
    ClienteYaRegistradoError,
    ClienteNoRegistradoError,
    ServicioYaRegistradoError,
    ServicioNoEncontradoError,
    RecursoYaRegistradoError,
    RecursoNoEncontradoError,
    ReservaYaRegistradaError,
    ReservaNoEncontradaError
)

class SistemaGestion:
    """Administra los clientes, servicios, recursos y reservas del sistema Software FJ."""
    
    def __init__(self):
        self._clientes = {}
        self._servicios = {}
        self._recursos = {}
        self._reservas = {}

    @property
    def clientes(self):
        return self._clientes   

    @property
    def servicios(self):
        return self._servicios

    @property
    def recursos(self):
        return self._recursos

    @property
    def reservas(self):
        return self._reservas
    
    # Bloque agregar cliente, servicio, recurso, reserva
    def registrar_cliente(self, cliente):
        """Agrega un cliente al sistema."""
        if not isinstance(cliente, Cliente):
            raise TypeError("Debe proporcionar un objeto de tipo Cliente.")
        if cliente.identificacion in self._clientes:
            raise ClienteYaRegistradoError(f"El cliente con Identificacion {cliente.identificacion} ya está registrado.")
        self._clientes[cliente.identificacion] = cliente

        Logger.registrar(
            "INFO",
            f"Cliente registrado: {cliente.identificacion} - {cliente.nombre}")
        
        return True  # Indica que el cliente se agregó correctamente

    def registrar_servicio(self, servicio):
        """Agrega un servicio al sistema."""
        if not isinstance(servicio, Servicio):
            raise TypeError("Debe proporcionar un objeto de tipo Servicio.")
        # Contar los servicios del mismo tipo
        cantidad_tipo = sum(
            1 for s in self._servicios.values()
            if type(s) == type(servicio))
        
        # Permitir un único servicio por tipo
        if cantidad_tipo >= 1:
            nombre_tipo = type(servicio).__name__.replace("Servicio", "")
            raise ServicioYaRegistradoError(
                f"No es posible registrar más servicios del tipo {nombre_tipo}. "
                f"Solo puede haber un servicio por tipo de servicio.")
               
        if servicio.identificador in self._servicios:
            raise ServicioYaRegistradoError(f"El servicio con ID {servicio.identificador} ya está registrado.")
        self._servicios[servicio.identificador] = servicio
        Logger.registrar(
            "INFO",
            f"Servicio registrado ({type(servicio).__name__}): "
            f"{servicio.identificador} - {servicio.nombre}"
)
        return True

    def registrar_recurso(self, recurso):
        """Agrega un recurso al sistema."""
        if not isinstance(recurso, Recurso):
            raise TypeError("Debe proporcionar un objeto de tipo Recurso.")

        # Contar los recursos del mismo tipo
        cantidad_tipo = sum(
            1 for r in self._recursos.values()
            if type(r) == type(recurso))

        # Permitir máximo dos recursos de cada tipo
        if cantidad_tipo >= 2:
            nombre_tipo = type(recurso).__name__.replace("Recurso", "")
            raise RecursoYaRegistradoError(
                f"No es posible registrar más recursos del tipo {nombre_tipo}. "
                f"Por el momento el límite es de 2 recursos por tipo de recurso.")
    
        if recurso.identificador in self._recursos:
            raise RecursoYaRegistradoError(f"El recurso con ID {recurso.identificador} ya está registrado.")
        self._recursos[recurso.identificador] = recurso
        Logger.registrar(
            "INFO",
            f"Recurso registrado ({type(recurso).__name__}): "
            f"{recurso.identificador} - {recurso.nombre}")
        return True  # Indica que el recurso se agregó correctamente

    def registrar_reserva(self, reserva):
        """Agrega una reserva al sistema."""
        if not isinstance(reserva, Reserva):
            raise TypeError("Debe proporcionar un objeto de tipo Reserva.")
        if reserva.identificador in self._reservas:
            raise ReservaYaRegistradaError(f"La reserva con ID {reserva.identificador} ya está registrada.")
        self._reservas[reserva.identificador] = reserva
        
        return True

    # ===============Bloque Buscar==================
    def buscar_cliente(self, identificacion):
        """Busca y devuelve un cliente registrado."""

        if not isinstance(identificacion, str):
            raise TypeError("La identificación debe ser una cadena de solo números.")

        identificacion = identificacion.strip()

        if identificacion not in self._clientes:
            raise ClienteNoRegistradoError(f"No existe un cliente con la identificación "
            f"{identificacion}.")
        
        return self._clientes[identificacion]
    

    def buscar_servicio(self, identificador):
        """Busca y devuelve un servicio registrado."""

        if not isinstance(identificador, str):
            raise TypeError("El identificador debe ser una cadena de texto")

        identificador = identificador.strip().upper()

        if identificador not in self._servicios:
            raise ServicioNoEncontradoError(f"No existe un servicio con id:" 
            f"{identificador}")
        
        return self._servicios[identificador]


    def buscar_recurso(self, identificador):
        """Busca y devuelve un recurso registrado."""

        if not isinstance(identificador, str):
            raise TypeError("El identificador debe ser una cadena de texto.")

        identificador = identificador.strip().upper()

        if identificador not in self._recursos:
            raise RecursoNoEncontradoError(f"No existe un recurso con el identificador "
            f"{identificador}.")

        return self._recursos[identificador]
    

    def buscar_reserva(self, identificador):
        """Busca y devuelve una reserva registrada."""

        if not isinstance(identificador, str):
            raise TypeError("El identificador debe ser una cadena de texto.")

        identificador = identificador.strip().upper()

        if identificador not in self._reservas:
            raise ReservaNoEncontradaError(f"No existe una reserva con el identificador "
            f"{identificador}.")

        return self._reservas[identificador]


    # ===============Bloque Listar==================
    def listar_clientes(self):
        """Devuelve una lista con todos los clientes registrados."""

        return list(self._clientes.values())

    def listar_servicios(self):
        """Devuelve una lista con todos los servicios registrados."""

        return list(self._servicios.values())

    def listar_recursos(self):
        """Devuelve una lista con todos los recursos registrados."""

        return list(self._recursos.values())

    def listar_reservas(self):
        """Devuelve una lista con todas las reservas registradas."""

        return list(self._reservas.values())


    def crear_reserva(
            self,
            identificador_reserva,
            identificacion_cliente,
            identificador_servicio,
            identificador_recurso,
            fecha,
            hora_inicio,
            duracion,
            impuesto=0,
            descuento=0):

        """Crea, procesa y registra una nueva reserva en el sistema."""

        # Buscar los objetos necesarios
        cliente = self.buscar_cliente(identificacion_cliente)
        servicio = self.buscar_servicio(identificador_servicio)
        recurso = self.buscar_recurso(identificador_recurso)

        # Crear la reserva
        reserva = Reserva(
            identificador_reserva,
            cliente,
            servicio,
            recurso,
            fecha,
            hora_inicio,
            duracion
        )

        # Procesar la reserva
        reserva.procesar(impuesto, descuento)

        # Registrar la reserva
        self.registrar_reserva(reserva)
        Logger.registrar(
            "INFO",
            f"Reserva creada: {reserva.identificador} | "
            f"Cliente: {reserva.cliente.identificacion} | "
            f"Servicio: {reserva.servicio.identificador} | "
            f"Recurso: {reserva.recurso.identificador}"
        )

        return reserva
