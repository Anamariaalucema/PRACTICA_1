from datetime import date, time, datetime
class Mesa: 
    def __init__(self, numero, capacidad, disponible) -> None:
        self.numero : int= numero
        self.capacidad : int = capacidad 
        self.disponible : bool = capacidad 

class InformacionContacto: 
    def __init__(self, nombre, numero, apellido, correo, telefono) -> None:
        self.nombre : str = nombre
        self.numero : str = numero
        self.apellido : str = apellido 
        self.correo : str = correo 
        self.telefono : float = telefono 

class Reserva: 
    def __init__(self, numero, fecha, hora, num_comensales, cliente) -> None:
        self.numero: int = numero 
        self.fecha : datetime = fecha 
        self.hora : datetime.time = hora 
        self.num_comensales : int = num_comensales 
        self.cliente: InformacionContacto = cliente 

class ConfirmarReserva: 
    def __init__(self, reserva, mesa, confirmado) -> None:
        self.reserva : Reserva = reserva 
        self.mesa : Mesa = mesa 
        self.confirmado : bool = confirmado 

class EvaluarServicio: 
    def __init__(self, puntuacion, comentarios) -> None:
        self.puntuacion : int = puntuacion 
        self.comentarios : str = comentarios  

    def dejar_comentario(self): 
        pass 

    def dejar_puntuacion(self): 
        pass 

class Restaurante: 
    def __init__(self, capacidad, reservas) -> None:
        self.capaidad : int = capacidad
        self.reservas : list[Reserva]

class SalaDeEspera: 
    def __init__(self, capacidad, clentes, hora_de__legada, ) -> None:
        self.capacidad : int = capacidad
        self.clientes : list[str] 
        self.hora_de_llegada = list[datetime.time] 

    def eliminar_reserva(self): 
        pass 

    def agregar_reserva(self): 
        pass 

class ControlarReservas: 
    def __init__(self, restaurante) -> None:
        self.restaurante : Restaurante = restaurante 
        
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
        fecha = datetime.datetime.strptime(fecha_input, '%d/%m/%Y')
        hora = datetime.datetime.strptime(hora_input, '%H:%M').time()
        return {"fecha": fecha, "hora": hora}
    
    # Función para verificar la disponibilidad del restaurante para una reserva
    def verificar_disponibilidad_reserva(self, fecha, hora, numero_comensales):
        # Verificar la capacidad del restaurante
        capacidad_disponible = self.CAPACIDAD_RESTAURANTE - sum(r["numero_comensales"] for r in self.reservas if r["fecha"] == fecha and r["hora"] == hora)
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
            reserva = {"nombre": informacion_contacto["nombre"], "numero": informacion_contacto["numero"], "correo": informacion_contacto["correo"], "fecha": fecha_hora_reserva["fecha"], "hora": fecha_hora_reserva["hora"], "numero_comensales": numero_comensales}
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
        
        