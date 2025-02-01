class Bus:
    def __init__(self, id_bus, capacidad):
        self.id_bus = id_bus
        self.capacidad = capacidad
        self.ruta = None
        self.horario = None
        self.conductor = None
        self.tickets_vendidos = 0
    
    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        self.horario = horario

    def vender_ticket(self):
        if self.tickets_vendidos < self.capacidad:
            self.tickets_vendidos += 1
            return True
        else:
            return False
    
    def __str__(self):
        return (f"Bus ID: {self.id_bus}, Capacidad: {self.capacidad}, Ruta: {self.ruta}, "
                f"Horario: {self.horario}, Conductor: {self.conductor}, Tickets Vendidos: {self.tickets_vendidos}")

class Conductor:
    def __init__(self, id_conductor, nombre, licencia):
        self.id_conductor = id_conductor
        self.nombre = nombre
        self.licencia = licencia
        self.horarios = []
    
    def asignar_horario(self, horario):
        if horario in self.horarios:
            return False
        self.horarios.append(horario)
        return True
    
    def __str__(self):
        return f"Conductor ID: {self.id_conductor}, Nombre: {self.nombre}, Licencia: {self.licencia}, Horarios: {self.horarios}"

def mostrar_menu():
    print("\nMenú de Administración:")
    print("1. Agregar Bus")
    print("2. Agregar Ruta a Bus")
    print("3. Registrar Horario a Bus")
    print("4. Agregar Conductor")
    print("5. Registrar Horario a Conductor")
    print("6. Asignar Bus a Conductor")
    print("7. Salir")

def agregar_bus(buses):
    id_bus = input("Ingrese el ID del Bus: ")
    capacidad = int(input("Ingrese la capacidad del Bus: "))
    bus = Bus(id_bus, capacidad)
    buses.append(bus)
    print("Bus registrado exitosamente")

def agregar_ruta_a_bus(buses):
    id_bus = input("Ingrese el ID del Bus: ")
    for bus in buses:
        if bus.id_bus == id_bus:
            ruta = input("Ingrese la ruta del Bus: ")
            bus.agregar_ruta(ruta)
            print("Ruta agregada exitosamente")
            return
    print("Bus no encontrado")

def registrar_horario_a_bus(buses):
    id_bus = input("Ingrese el ID del Bus: ")
    for bus in buses:
        if bus.id_bus == id_bus:
            horario = input("Ingrese el horario del Bus (formato HH:MM-HH:MM): ")
            bus.registrar_horario(horario)
            print("Horario registrado exitosamente")
            return
    print("Bus no encontrado")

def agregar_conductor(conductores):
    id_conductor = input("Ingrese el ID del Conductor: ")
    nombre = input("Ingrese el nombre del Conductor: ")
    licencia = input("Ingrese la licencia del Conductor: ")
    conductor = Conductor(id_conductor, nombre, licencia)
    conductores.append(conductor)
    print("Conductor registrado exitosamente")

def registrar_horario_a_conductor(conductores):
    id_conductor = input("Ingrese el ID del Conductor: ")
    for conductor in conductores:
        if conductor.id_conductor == id_conductor:
            horario = input("Ingrese el horario del Conductor (formato HH:MM-HH:MM): ")
            if conductor.asignar_horario(horario):
                print("Horario registrado exitosamente")
            else:
                print("Horario ya asignado a este conductor")
            return
    print("Conductor no encontrado")

def asignar_bus_a_conductor(buses, conductores):
    id_bus = input("Ingrese el ID del Bus: ")
    id_conductor = input("Ingrese el ID del Conductor: ")
    
    bus = None
    conductor = None
    
    for b in buses:
        if b.id_bus == id_bus:
            bus = b
            break
    
    for c in conductores:
        if c.id_conductor == id_conductor:
            conductor = c
            break
    
    if bus and conductor:
        if bus.horario in conductor.horarios:
            print("Conductor ya asignado a este horario")
        else:
            bus.conductor = conductor.nombre
            conductor.horarios.append(bus.horario)
            print("Bus asignado al conductor exitosamente")
    else:
        print("Bus o Conductor no encontrado")

def menu():
    buses = []
    conductores = []
    
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            agregar_bus(buses)
        elif opcion == "2":
            agregar_ruta_a_bus(buses)
        elif opcion == "3":
            registrar_horario_a_bus(buses)
        elif opcion == "4":
            agregar_conductor(conductores)
        elif opcion == "5":
            registrar_horario_a_conductor(conductores)
        elif opcion == "6":
            asignar_bus_a_conductor(buses, conductores)
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Llamar a la función principal del menú
menu()