


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

    #Uso de propiedades getter y setter para encapsular los atributos y permitir validaciones al establecer valores. 
    # Esto permite controlar el acceso a los atributos de la clase Cliente de manera controlada.
    @property
    def identificacion(self):
        return self._identificacion
        
    @property
    def nombre(self):
        return self._nombre
        
    #Verifica que el nombre no esté vacío. Si el nombre está vacío, se lanza una excepción ValueError con un mensaje indicando que el nombre del cliente no puede estar vacío.
    @nombre.setter
    def nombre(self, nuevo_nombre):
        
    # Validar que el nombre sea una cadena de texto
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        nuevo_nombre = nuevo_nombre.strip()
        if not nuevo_nombre:
            raise ValueError("El nombre del cliente no puede estar vacío.")              
        self._nombre = nuevo_nombre
        
        
    @property
    def telefono(self):
        return self._telefono
            
    #Verifica que el teléfono tenga exactamente 10 dígitos y que solo contenga números. Si no cumple con estas condiciones, se lanza la excepción TelefonoInvalidoError.
            
    def _validar_telefono(self, telefono):
        if not isinstance(telefono, str):
            raise TypeError("El teléfono debe ser una cadena de texto.")        
        telefono = telefono.strip()
        if not telefono.isdigit() or len(telefono) != 10:
            raise TelefonoInvalidoError(telefono)
        return telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
            
        self._telefono = self._validar_telefono(nuevo_telefono)


    @property
    def correo(self):
        return self._correo
    #Verifica que el correo contenga un '@'. Si no lo contiene, se lanza una excepción ValueError con un mensaje indicando que el correo electrónico debe contener un '@'.
    @correo.setter
    def correo(self, nuevo_correo):
        if not isinstance(nuevo_correo, str):
            raise TypeError("El correo debe ser una cadena de texto.")  
        nuevo_correo = nuevo_correo.strip().lower()  # Eliminar espacios en blanco al inicio y al final
        if "@" not in nuevo_correo:
            raise ValueError("El correo electrónico debe contener un '@'.")
        self._correo = nuevo_correo


        #Sobrescribe el método __str__ para proporcionar una representación legible del objeto Cliente. Esto es útil para imprimir información sobre el cliente de manera clara y concisa.
        def __str__(self):
    
            return (
                f"Cliente: {self.nombre} "
                f"(Identificacion: {self.identificacion})")
    