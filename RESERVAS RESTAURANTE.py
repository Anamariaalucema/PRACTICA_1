import datetime

# Capacidad del restaurante
CAPACIDAD_RESTAURANTE = 50

# Lista de reservas
reservas = []

# Función para solicitar información de contacto del usuario
def obtener_informacion_contacto():
    nombre = input("Ingrese su nombre: ")
    numero = input("Ingrese su número de teléfono: ")
    correo = input("Ingrese su correo electrónico: ")
    return {"nombre": nombre, "numero": numero, "correo": correo}

# Función para solicitar el número de comensales
def obtener_numero_comensales():
    return int(input("Ingrese el número de comensales: "))

# Función para solicitar la fecha y hora de la reserva
def obtener_fecha_hora_reserva():
    fecha_input = input("Ingrese la fecha de la reserva (en formato dd/mm/aaaa): ")
    hora_input = input("Ingrese la hora de la reserva (en formato hh:mm): ")
    fecha = datetime.datetime.strptime(fecha_input, '%d/%m/%Y')
    hora = datetime.datetime.strptime(hora_input, '%H:%M').time()
    return {"fecha": fecha, "hora": hora}

# Función para verificar la disponibilidad del restaurante para una reserva
def verificar_disponibilidad_reserva(fecha, hora, numero_comensales):
    # Verificar la capacidad del restaurante
    capacidad_disponible = CAPACIDAD_RESTAURANTE - sum(r["numero_comensales"] for r in reservas if r["fecha"] == fecha and r["hora"] == hora)
    if numero_comensales <= capacidad_disponible:
        return True
    else:
        return False

# Función para realizar una reserva
def hacer_reserva():
    informacion_contacto = obtener_informacion_contacto()
    numero_comensales = obtener_numero_comensales()
    fecha_hora_reserva = obtener_fecha_hora_reserva()
    disponible = verificar_disponibilidad_reserva(fecha_hora_reserva["fecha"], fecha_hora_reserva["hora"], numero_comensales)
    if disponible:
        reserva = {"nombre": informacion_contacto["nombre"], "numero": informacion_contacto["numero"], "correo": informacion_contacto["correo"], "fecha": fecha_hora_reserva["fecha"], "hora": fecha_hora_reserva["hora"], "numero_comensales": numero_comensales}
        reservas.append(reserva)
        print("Reserva realizada con éxito.")
    else:
        print("Lo siento, no hay capacidad disponible para la fecha y hora solicitadas.")

# Función principal
def main():
    while True:
        opcion = input("Ingrese '1' para hacer una reserva o '0' para salir: ")
        if opcion == '1':
            hacer_reserva()
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()