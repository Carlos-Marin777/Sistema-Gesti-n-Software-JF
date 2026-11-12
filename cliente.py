


from excepciones import IdentificacionInvalidaError, TelefonoInvalidoError


class Cliente:
    """Representa un cliente registrado en el sistema Software FJ."""


    def __init__(self, identificacion, nombre, telefono, correo):
        #Validacion de la identificación del cliente. Se asegura de que sea una cadena de texto, no esté vacía y contenga solo números. Si alguna de estas condiciones no se cumple, se lanza una excepción correspondiente.
        if not isinstance(identificacion, str):
            raise TypeError("La identificación debe ser una cadena de texto.")
        identificacion = identificacion.strip()
        if not identificacion:
            raise IdentificacionInvalidaError("La identificación del cliente no puede estar vacía.")
        if not identificacion.isdigit():
            raise IdentificacionInvalidaError(f"La identificación '{identificacion}' no es válida. Debe contener solo números.")
        self._identificacion = identificacion

        self.nombre = nombre    
        self.telefono = telefono
        self.correo = correo
        