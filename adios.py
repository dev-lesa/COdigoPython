class Vehiculo:
    def __init__(self, matricula, modelo, num_llantas):
        self.matricula = matricula
        self.modelo = modelo
        self.num_llantas = num_llantas

    def velocidad_permitida(self):
        pass

    def mostrar_info_base(self):
        print(f"Matricula: {self.matricula}")
        print(f"Modelo: {self.modelo}")
        print(f"Llantas: {self.num_llantas}")

class Taxi(Vehiculo):
    def __init__(self, matricula, modelo, num_llantas, licencia, pasajeros):
        super().__init__(matricula, modelo, num_llantas)
        self.licencia = licencia
        self.pasajeros = pasajeros

    def velocidad_permitida(self):
        if self.pasajeros == 0:
            return 80
        else:
            return 70

    def mostrar_info(self):
        self.mostrar_info_base()
        print(f"Licencia: {self.licencia}")
        print(f"Pasajeros: {self.pasajeros}")
        print(f"Velocidad permitida: {self.velocidad_permitida()} km/h\n")

class Bus(Vehiculo):
    def __init__(self, matricula, modelo, num_llantas, plazas, pasajeros):
        super().__init__(matricula, modelo, num_llantas)
        self.plazas = plazas
        self.pasajeros = pasajeros

    def velocidad_permitida(self):
        if self.pasajeros == 0:
            return 60
        else:
            return 40

    def mostrar_info(self):
        self.mostrar_info_base()
        print(f"Plazas: {self.plazas}")
        print(f"Pasajeros: {self.pasajeros}")
        print(f"Velocidad permitida: {self.velocidad_permitida()} km/h\n")

taxi1 = Taxi("ABC123", "Nissan", 4, "LIC001", 0)
taxi1.mostrar_info()
taxi2 = Taxi("XYZ789", "Chevrolet", 4, "LIC002", 3)
taxi2.mostrar_info()
bus1 = Bus("VEG777", "LoboDomesticado", 6, 40, 0)
bus1.mostrar_info()
bus2 = Bus("ALEJ124", "Mercedes", 6, 50, 25)
bus2.mostrar_info()


