# Integrantes: Carlos Daniel Marin Amaris
#
#
#
#
# Grupo: 213023
# Programa: Ingenieria de Sistemas
# Curso: Programacion
# Centro: CEAD Valledupar
# Codigo fuente: autoria propia

class ErrorSistemaFJ(Exception):
    """ Clase base para todas las excepciones del sistema Software FJ.""" 
    pass

class ErrorCliente(ErrorSistemaFJ):
    """ Agrupa todas las excepciones relacionadas con clientes."""
    pass

class ErrorReserva(ErrorSistemaFJ):
    """ Agrupa todas las excepciones relacionadas con reservas."""
    pass

class ErrorRecurso(ErrorSistemaFJ):
    """Agrupa todas las excepciones relacionadas con recursos."""
    pass

class ErrorHorario(ErrorSistemaFJ):
    """Agrupa todas las excepciones relacionadas con horarios."""
    pass

class ErrorServicio(ErrorSistemaFJ):
    """Agrupa todas las excepciones relacionadas con servicios."""
    pass
#===================================================#
#Rama de errores de excepcion para la clase cliente 
#===================================================#
class ClienteNoRegistradoError(ErrorCliente):
    """esta Excepcion se produce cuando se intenta crear una reserva para un cliente que no existe en el sistema."""
    pass

class IdentificacionInvalidaError(ErrorCliente):
    """Identificacion invalida."""
    pass

class TelefonoInvalidoError(ErrorCliente):
    """ Telefono invalido."""
    def __init__(self, telefono):

        super().__init__(f"El teléfono '{telefono}' no es válido.")

class ClienteYaRegistradoError(ErrorCliente):
    """ Cliente ya registrado."""
    pass
#=============================================================#
# Rama de errores de excepcion que tienen que ver con horarios
#=============================================================#
class FormatoHoraInvalidoError(ErrorHorario):
    """ La hora no tiene un formato válido. """
    pass

class HorarioInvalidoError(ErrorHorario):
    """La hora de inicio y la hora de fin forman un intervalo incorrecto."""
    pass

class HorarioFueraDeServicioError(ErrorHorario):
    """El horario solicitado está fuera del horario de atención del negocio."""
    pass

class FormatoFechaInvalidoError(ErrorHorario):
    """La fecha no tiene un formato válido."""
    pass
#=============================================================#
# Rama de errores de excepcion que tienen que ver con recursos
#=============================================================#
class RecursoNoDisponibleError(ErrorRecurso):
    """El recurso existe, pero actualmente no puede utilizarse."""
    pass

class RecursoYaRegistradoError(ErrorRecurso):
    """Se lanza cuando se intenta registrar un recurso ya existente."""
    pass

class RecursoNoEncontradoError(ErrorRecurso):
    """El recurso solicitado no existe."""
    pass
#=============================================================#
# Rama de errores de excepcion que tienen que ver con servicios
#=============================================================#
class ServicioNoDisponibleError(ErrorServicio):
    """El servicio solicitado no puede prestarse actualmente."""
    pass

class ServicioNoEncontradoError(ErrorServicio):
    """El servicio solicitado no existe"""
    pass

class ServicioYaRegistradoError(ErrorServicio):
    """Se lanza cuando se intenta registrar un servicio ya existente."""
    pass
#============================================================#
# Rama de errores de excepcion que tienen que ver con reservas
#============================================================#
class ReservaNoEncontradaError(ErrorReserva):
    """La reserva solicitada no existe."""
    pass
class ReservaYaRegistradaError(ErrorReserva):
    """Se lanza cuando se intenta registrar una reserva ya existente."""
    pass

class ReservaYaCanceladaError(ErrorReserva):
    """La reserva ya fue cancelada anteriormente."""
    pass

class ReservaYaFinalizadaError(ErrorReserva):
    """La reserva ya terminó y no admite más modificaciones."""
    pass

class ReservaYaConfirmadaError(ErrorReserva):
    """La reserva ya fue confirmada y no puede modificarse."""
    pass

