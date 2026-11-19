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


# Importaciones
from sistema_gestion import SistemaGestion

from cliente import Cliente

from sala import Sala
from equipo import Equipo
from asesor import Asesor

from servicio_sala import ServicioSala
from servicio_equipo import ServicioEquipo
from servicio_asesoria import ServicioAsesoria

from excepciones import ErrorSistemaFJ

from logger import Logger 



# Creacion de sistema 
sistema = SistemaGestion()


def registrar_cliente():
    """Solicita los datos de un cliente y lo registra en el sistema."""

    try:
        print("\n=== REGISTRAR CLIENTE ===")

        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo electrónico: ")

        cliente = Cliente(
            identificacion,
            nombre,
            telefono,
            correo
        )

        sistema.registrar_cliente(cliente)


    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
        Logger.registrar("ERROR", f"Error inesperado: {error}")
        print(f"\nError inesperado: {error}")

    else:
        print("\nCliente registrado correctamente.")

    finally:
        input("\nPresione ENTER para continuar...")


def registrar_servicio():
    """Solicita los datos de un servicio y lo registra en el sistema."""

    try:
        print("\n=== REGISTRAR SERVICIO ===")

        print("\n===Tipos de servicios posibles===" \
        "\nSolo se permite la creacion de 1 servicio por tipo:")
        print("1. Reserva de Sala")
        print("2. Alquiler de Equipo")
        print("3. Asesoría Especializada")

        opcion = input("\nSeleccione una de las opciones " 
        "\npara crear un tipo de servicio: ")

        identificador = input("ID del servicio: ")
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        tarifa = float(input("Tarifa por hora: "))

        if opcion == "1":
            servicio = ServicioSala(
                identificador,
                nombre,
                descripcion,
                tarifa
            )

        elif opcion == "2":
            servicio = ServicioEquipo(
                identificador,
                nombre,
                descripcion,
                tarifa
            )

        elif opcion == "3":
            servicio = ServicioAsesoria(
                identificador,
                nombre,
                descripcion,
                tarifa
            )

        else:
            print("\nOpción inválida.")
            return

        sistema.registrar_servicio(servicio)
       

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except ValueError:
        print("\nERROR: La tarifa debe ser un valor numérico.")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    else:
        print("\nServicio registrado correctamente." \
                "\nA partir de este momento no podrán registrarse más servicios de este tipo.")

    finally:
        input("\nPresione ENTER para continuar...")



def registrar_recurso():
    """Solicita los datos de un recurso y lo registra en el sistema."""

    try:
        print("\n=== REGISTRAR RECURSO ===")

        print("\n==Tipos de recursos posibles==" \
        "\nSolo se permite la creacion de 2 recursos por tipo:")
        print("1. Sala")
        print("2. Equipo")
        print("3. Asesor")

        opcion = input("\nSeleccione una de las opciones " 
        "\npara crear un recurso: ")

        identificador = input("ID del recurso: ")
        nombre = input("Nombre: ")

        if opcion == "1":

            capacidad = int(input("Capacidad de la sala: "))

            recurso = Sala(
                identificador,
                nombre,
                capacidad
            )

        elif opcion == "2":

            tipo_equipo = input("Elija tipo de equipo: ")

            recurso = Equipo(
                identificador,
                nombre,
                tipo_equipo
            )

        elif opcion == "3":

            especialidad = input("Especialidad del asesor: ")

            recurso = Asesor(
                identificador,
                nombre,
                especialidad
            )

        else:
            print("\nOpción inválida.")
            return

        sistema.registrar_recurso(recurso)

        
    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except ValueError:
        print("\nERROR: Se ingresó un valor con formato incorrecto.")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    else:
        print("\nRecurso registrado correctamente.")

    finally:
        input("\nPresione ENTER para continuar...")



def crear_reserva():
    """Solicita los datos de una reserva y la registra en el sistema."""

    try:
        print("\n=== CREAR RESERVA ===")

        identificador = input("ID de la reserva          : ")
        identificacion_cliente = input("Identificación del cliente: ")
        identificador_servicio = input("ID del servicio           : ")
        identificador_recurso = input("ID del recurso            : ")
        fecha = input("Fecha (AAAA-MM-DD)        : ")
        hora_inicio = input("Hora de inicio (HH:MM)    : ")
        duracion = float(input("Duración (horas)          : "))
        impuesto = float(input("Impuesto (%)              : "))
        descuento = float(input("Descuento (%)             : "))

        reserva = sistema.crear_reserva(
            identificador,
            identificacion_cliente,
            identificador_servicio,
            identificador_recurso,
            fecha,
            hora_inicio,
            duracion,
            impuesto,
            descuento
        )

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")
    
    except ValueError:
        print("\nERROR: La duración, el impuesto y el descuento deben ser valores numéricos.")
    
    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")   

    else:    
        print("\n" + "=" * 32)
        print("RESERVA CREADA CORRECTAMENTE")
        print("=" * 32)
        print(f"ID Reserva : {reserva.identificador}\n"
              f"Cliente    : {reserva.cliente.nombre}\n"
              f"Servicio   : {reserva.servicio.nombre}\n"
              f"Recurso    : {reserva.recurso.nombre}\n"
              f"Estado     : {reserva.estado}\n"
              f"Costo total: ${reserva.costo_total:,.2f}")

    finally:
        input("\nPresione ENTER para continuar...")

    

def buscar_cliente():
    """Busca un cliente por su identificación."""

    try:
        print("\n=== BUSCAR CLIENTE ===")

        identificacion = input("Ingrese la identificación del cliente: ")

        cliente = sistema.buscar_cliente(identificacion)

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    else:
        print("\nCliente encontrado:")
        print(cliente)

    finally:
        input("\nPresione ENTER para continuar...")

    

def buscar_servicio():
    """Busca un servicio por su identificador."""

    try:
        print("\n=== BUSCAR SERVICIO ===")

        identificador = input("Ingrese el ID del servicio: ")

        servicio = sistema.buscar_servicio(identificador)

        

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    else:  
        print("\nServicio encontrado:")
        print(servicio)

    finally:
        input("\nPresione ENTER para continuar...")


def buscar_recurso():
    """Busca un recurso por su identificador."""

    try:
        print("\n=== BUSCAR RECURSO ===")

        identificador = input("Ingrese el ID del recurso: ")

        recurso = sistema.buscar_recurso(identificador)
       

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    else:
        print("\nRecurso encontrado:")
        print(recurso)

    finally:
        input("\nPresione ENTER para continuar...")



def buscar_reserva():
    """Busca una reserva por su identificador."""

    try:
        print("\n=== BUSCAR RESERVA ===")

        identificador = input("Ingrese el ID de la reserva: ")

        reserva = sistema.buscar_reserva(identificador)

        
    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    else:
        print("\nReserva encontrada:")
        print(reserva)
        
    finally:
        input("\nPresione ENTER para continuar...")


def listar_clientes():
    """Muestra todos los clientes registrados."""

    try:
        print("\n=== LISTA DE CLIENTES ===")

        clientes = sistema.listar_clientes()

        if not clientes:
            print("\nNo hay clientes registrados.")
            return

        for cliente in clientes:
            print("-" * 40)
            print(cliente)

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    finally:
        input("\nPresione ENTER para continuar...")


def listar_servicios():
    """Muestra todos los servicios registrados."""

    try:
        print("\n==== SERVICIOS DISPONIBLES DE SOFTWARE FJ ====")

        servicios = sistema.listar_servicios()

        if not servicios:
            print("\nNo hay servicios registrados.")
            return

        for servicio in servicios:
            print("-" * 50)
            print(servicio.describir_servicio())

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    finally:
        input("\nPresione ENTER para continuar...")



def listar_recursos():
    """Muestra todos los recursos registrados."""

    try:
        print("\n=== LISTA DE RECURSOS ===")

        recursos = sistema.listar_recursos()

        if not recursos:
            print("\nNo hay recursos registrados.")
            return

        for recurso in recursos:
            print("-" * 40)
            print(recurso.describir_recurso())

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    finally:
        input("\nPresione ENTER para continuar...")


def listar_reservas():
    """Muestra todas las reservas registradas."""

    try:
        print("\n=== LISTA DE RESERVAS ===")

        reservas = sistema.listar_reservas()

        if not reservas:
            print("\nNo hay reservas registradas.")
            return

        for reserva in reservas:
            print("-" * 40)
            print(reserva)

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    finally:
        input("\nPresione ENTER para continuar...")


def cancelar_reserva():
    """Cancela una reserva registrada."""

    try:
        print("\n=== CANCELAR RESERVA ===")

        identificador = input("ID de la reserva: ")

        reserva = sistema.buscar_reserva(identificador)

        reserva.cancelar()


    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    else:
        print("\nReserva cancelada correctamente.")

    finally:
        input("\nPresione ENTER para continuar...")


def finalizar_reserva():
    """Finaliza una reserva registrada."""

    try:
        print("\n=== FINALIZAR RESERVA ===")

        identificador = input("ID de la reserva: ")

        reserva = sistema.buscar_reserva(identificador)

        reserva.finalizar()
     

    except ErrorSistemaFJ as error:
        Logger.registrar("ERROR", str(error))
        print(f"\nERROR: {error}")

    except Exception as error:
            Logger.registrar("ERROR", f"Error inesperado: {error}")
            print(f"\nError inesperado: {error}")

    else:
        print("\nReserva finalizada correctamente.")

    finally:
        input("\nPresione ENTER para continuar...")



def mostrar_menu():
    """Muestra el menú principal del sistema."""
    

    print("\n" + "=" * 32)
    print(" ↑↑↑  SISTEMA SOFTWARE FJ  ↑↑↑")
    print("=" * 32)
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Registrar recurso")
    print("4. Crear reserva")
    print("5. Buscar cliente")
    print("6. Buscar servicio")
    print("7. Buscar recurso")
    print("8. Buscar reserva")
    print("9. Listar clientes")
    print("10. Listar servicios")
    print("11. Listar recursos")
    print("12. Listar reservas")
    print("13. Cancelar reserva")
    print("14. Finalizar reserva")
    print("0. Salir")
    print("=" * 32)
    print("↑" * 32)


if __name__ == "__main__":

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "0":
            print("\nGracias por utilizar Software FJ.")
            Logger.registrar(
                "INFO",
                "El sistema fue cerrado correctamente."
            )
            break

        elif opcion == "1":
            registrar_cliente()

        elif opcion == "2":
            registrar_servicio()

        elif opcion == "3":
            registrar_recurso()

        elif opcion == "4":
            crear_reserva()

        elif opcion == "5":
            buscar_cliente()

        elif opcion == "6":
            buscar_servicio()


        elif opcion == "7":
            buscar_recurso()

        elif opcion == "8":
            buscar_reserva()

        elif opcion == "9":
            listar_clientes()

        elif opcion == "10":
            listar_servicios()

        elif opcion == "11":
            listar_recursos()

        elif opcion == "12":
            listar_reservas()

        elif opcion == "13":
            cancelar_reserva()

        elif opcion == "14":
            finalizar_reserva()

        else:
            print("\nOpción inválida. Intente nuevamente.")
