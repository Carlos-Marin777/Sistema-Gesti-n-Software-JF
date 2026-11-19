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


from datetime import datetime
import os


class Logger:
    """Escribe un evento o error en el archivo softwarefj.log con fecha y hora.."""

    
    RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
    ARCHIVO_LOG = os.path.join(RUTA_BASE, "softwarefj.log")

    @staticmethod
    def registrar(tipo, mensaje):
        """Registra un evento o error en el archivo de logs."""

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       

        with open(Logger.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            archivo.write(f"{fecha_hora} | {tipo.upper():<7} | {mensaje}\n")