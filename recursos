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


from abc import ABC, abstractmethod

class Recurso(ABC):
    """Clase base abstracta para los diferentes tipos de recursos ofrecidos por Software FJ."""
    def __init__(self, identificador, nombre, estado=True):

        # Validar que el identificador sea una cadena de texto
        if not isinstance(identificador, str):
            raise TypeError("El identificador debe ser una cadena de texto.")
        
        identificador = identificador.strip().upper()  # Convertir a mayúsculas y eliminar espacios en blanco

        if not identificador:
            raise ValueError("El identificador del recurso no puede estar vacío.")
        
        self._identificador = identificador
        

        self.nombre = nombre
        self.estado = estado  # True para disponible, False para no disponible

    @property
    def identificador(self):
        return self._identificador


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        # Validar que el nombre sea una cadena de texto
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        
        nuevo_nombre = nuevo_nombre.strip()
        if not nuevo_nombre:
            raise ValueError("El nombre del recurso no puede estar vacío.")
        self._nombre = nuevo_nombre
        

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        if not isinstance(nuevo_estado, bool):
            raise TypeError("El estado debe ser un valor booleano (True o False).")
        self._estado = nuevo_estado

    #Metodos abstractos para que las subclases implementen su propia lógica
    def disponible(self):
        """Verifica si el recurso está disponible."""
        return self.estado

    def __str__(self):
        estado = "Disponible" if self.estado else "No disponible"
        return (f"Recurso: {self.nombre} (ID: {self.identificador}) - Estado: {estado}")
        
    
    @abstractmethod
    def describir_recurso(self):
        """Devuelve una descripción del recurso."""
        pass

    @abstractmethod
    def validar_parametros(self):
        """Valida que los parámetros específicos del recurso sean correctos."""
        pass
