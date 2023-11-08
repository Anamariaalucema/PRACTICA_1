from restaurante import *
from tkinter import Tk, Label, Button

class InterfazGrafica:
    def __init__(self, control_reservas):
        self.control_reservas = control_reservas

        self.ventana = Tk()
        self.ventana.title("Reservas de Restaurante")

        self.etiqueta = Label(self.ventana, text="Bienvenido al sistema de reservas de restaurante")
        self.etiqueta.pack()

        self.boton_reserva = Button(self.ventana, text="Hacer Reserva", command=self.control_reservas.hacer_reserva)
        self.boton_reserva.pack()

        self.boton_salir = Button(self.ventana, text="Salir", command=self.ventana.quit)
        self.boton_salir.pack()

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == '__main__':
    restaurante = Restaurante(ControlarReservas.CAPACIDAD_RESTAURANTE, ControlarReservas.reservas)
    control_reservas = ControlarReservas(restaurante)
    interfaz = InterfazGrafica(control_reservas)
    interfaz.iniciar()
