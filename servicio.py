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

from abc import ABC, abstractmethod



class Servicio(ABC):
    """Clase base abstracta para los diferentes tipos de servicios ofrecidos por Software FJ."""
    def __init__(self, identificador, nombre, descripcion, estado=True):


        # Validar que el identificador sea una cadena de texto
        if not isinstance(identificador, str):
            raise TypeError("El identificador debe ser una cadena de texto.")
        identificador = identificador.strip().upper()  # Convertir a mayúsculas y eliminar espacios en blanco
        if not identificador:
            raise ValueError("El identificador del servicio no puede estar vacío.")

        self._identificador = identificador

        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado  # True para disponible, False para no disponible


    #Uso de propiedades para encapsular los atributos y permitir validaciones al establecer valores
    @property
    def identificador(self):
        return self._identificador
    
    
    @property #Encapsulamiento del atributo identificador para que sea de solo lectura, evitando que se modifique después de la creación del objeto.
    def nombre(self):
        return self._nombre
    
    @nombre.setter #Método setter para establecer el nombre del servicio. Se asegura de que el nombre no esté vacío y elimina espacios en blanco al inicio y al final.
    def nombre(self, nuevo_nombre):
    
        # Validar que el nombre sea una cadena de texto
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
    
        nuevo_nombre = nuevo_nombre.strip()
        if not nuevo_nombre:
            raise ValueError("El nombre del servicio no puede estar vacío.")
        self._nombre = nuevo_nombre    


    @property
    def descripcion(self):
        return self._descripcion    
    
    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        # Validar que la descripcion sea una cadena de texto
        if not isinstance(nueva_descripcion, str):
            raise TypeError("la descripcion debe ser una cadena de texto.")
    
        nueva_descripcion = nueva_descripcion.strip()
            
        if not nueva_descripcion:
            raise ValueError("La descripción del servicio no puede estar vacía.")
        self._descripcion = nueva_descripcion
    
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        if not isinstance(nuevo_estado, bool):
            raise TypeError("El estado debe ser un valor booleano (True o False).")
        self._estado = nuevo_estado
    
    
    def _validar_tarifa(self, tarifa):
        """Valida que la tarifa del servicio sea un número positivo. Este método es reutilizado por todos los servicios derivados."""
    
        if not isinstance(tarifa, (int, float)) or isinstance(tarifa, bool):
            raise TypeError("La tarifa por hora debe ser un numero.")
        if tarifa <= 0:
            raise ValueError("La tarifa debe ser un valor númerico positivo.")
        return tarifa
    
    def _validar_duracion(self, duracion):
            """Método privado para validar la duración de la reserva. Se asegura de que la duración sea un número positivo."""
            if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
                raise TypeError("La duración debe ser un número.")
            if duracion <= 0:
                raise ValueError("La duración debe ser un valor númerico positivo.")
            return duracion
    
    
    def __str__(self): #Sobrescribe el método __str__ para proporcionar una representación legible del objeto Servicio. Esto es útil para imprimir información sobre el servicio de manera clara y concisa.
        estado = "Disponible" if self.estado else "No disponible"
        return (
            f"Servicio: {self.nombre} " 
            f"(ID: {self.identificador}) - {estado}")
    
    # Métodos abstractos que deben ser implementados por las subclases. Estos métodos definen la interfaz que todas las clases derivadas deben seguir.

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo del servicio.
        Args:
            duracion (int | float): Duración de la reserva en horas.
            impuesto (float): Porcentaje de impuesto expresado en decimal   (opcional).
            descuento (float): Porcentaje de descuento expresado en decimal (opcional).
        Returns:
        float: Costo total del servicio
        """
        pass   
        
    @abstractmethod
    def describir_servicio(self):
        """Devuelve una descripción del servicio."""
        pass
        
    @abstractmethod
    def validar_parametros(self):
        """Valida los parámetros específicos del servicio."""
        pass