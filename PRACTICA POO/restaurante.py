from datetime import datetime, time
from typing import List

class Mesa:
    def __init__(self, numero: int, capacidad: int, disponible: bool) -> None:
        self.numero = numero
        self.capacidad = capacidad
        self.disponible = disponible

class InformacionContacto:
    def __init__(self, nombre: str, numero: str, apellido: str, correo: str, telefono: float) -> None:
        self.nombre = nombre
        self.numero = numero
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

class Reserva:
    def __init__(self, numero: int, fecha: datetime, hora: time, num_comensales: int, cliente: InformacionContacto) -> None:
        self.numero = numero
        self.fecha = fecha
        self.hora = hora
        self.num_comensales = num_comensales
        self.cliente = cliente

class ConfirmarReserva:
    def __init__(self, reserva: Reserva, mesa: Mesa, confirmado: bool) -> None:
        self.reserva = reserva
        self.mesa = mesa
        self.confirmado = confirmado

class EvaluarServicio:
    def __init__(self, puntuacion: int, comentarios: str) -> None:
        self.puntuacion = puntuacion
        self.comentarios = comentarios

    def dejar_comentario(self):
        pass

    def dejar_puntuacion(self):
        pass

class Restaurante:
    def __init__(self, capacidad: int, reservas: List[Reserva]) -> None:
        self.capacidad = capacidad
        self.reservas = reservas

class SalaDeEspera:
    def __init__(self, capacidad: int, clientes: List[str], hora_de_llegada: List[time]) -> None:
        self.capacidad = capacidad
        self.clientes = clientes
        self.hora_de_llegada = hora_de_llegada

    def eliminar_reserva(self):
        pass

    def agregar_reserva(self):
        pass

class ControlarReservas:
    def __init__(self, restaurante: Restaurante) -> None:
        self.restaurante = restaurante

    # Capacidad del restaurante
    CAPACIDAD_RESTAURANTE = 50

    # Lista de reservas
    reservas = []

    # Función para solicitar información de contacto del usuario
    def obtener_informacion_contacto(self):
        nombre = input("Ingrese su nombre: ")
        numero = input("Ingrese su número de teléfono: ")
        correo = input("Ingrese su correo electrónico: ")
        return {"nombre": nombre, "numero": numero, "correo": correo}

    # Función para solicitar el número de comensales
    def obtener_numero_comensales(self):
        return int(input("Ingrese el número de comensales: "))

    # Función para solicitar la fecha y hora de la reserva
    def obtener_fecha_hora_reserva(self):
        fecha_input = input("Ingrese la fecha de la reserva (en formato dd/mm/aaaa): ")
        hora_input = input("Ingrese la hora de la reserva (en formato hh:mm): ")
        fecha = datetime.strptime(fecha_input, '%d/%m/%Y')
        hora = datetime.strptime(hora_input, '%H:%M').time()
        return {"fecha": fecha, "hora": hora}

    # Función para verificar la disponibilidad del restaurante para una reserva
    def verificar_disponibilidad_reserva(self, fecha, hora, numero_comensales):
        # Verificar la capacidad del restaurante
        capacidad_disponible = self.CAPACIDAD_RESTAURANTE - sum(r.num_comensales for r in self.reservas if r.fecha == fecha and r.hora == hora)
        if numero_comensales <= capacidad_disponible:
            return True
        else:
            return False

    # Función para realizar una reserva
    def hacer_reserva(self):
        informacion_contacto = self.obtener_informacion_contacto()
        numero_comensales = self.obtener_numero_comensales()
        fecha_hora_reserva = self.obtener_fecha_hora_reserva()
        disponible = self.verificar_disponibilidad_reserva(fecha_hora_reserva["fecha"], fecha_hora_reserva["hora"], numero_comensales)
        if disponible:
            reserva = Reserva(len(self.reservas) + 1, fecha_hora_reserva["fecha"], fecha_hora_reserva["hora"], numero_comensales, informacion_contacto)
            self.reservas.append(reserva)
            print("Reserva realizada con éxito.")
        else:
            print("Lo siento, no hay capacidad disponible para la fecha y hora solicitadas.")

    # Función principal
    def main(self):
        while True:
            opcion = input("Ingrese '1' para hacer una reserva o '0' para salir: ")
            if opcion == '1':
                self.hacer_reserva()
            elif opcion == '0':
                break
            else:
                print("Opción no válida.")

if __name__ == '__main__':
    restaurante = Restaurante(ControlarReservas.CAPACIDAD_RESTAURANTE, ControlarReservas.reservas)
    control_reservas = ControlarReservas(restaurante)
    control_reservas.main()
