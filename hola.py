class Animal:
    def __init__(self,nombre):
        self.nombre= nombre

    def hacer_sonido(self):
        return "sonido generico"

class Perro(Animal): 
    def hacer_sonido(self):
        return "¡Guau guau!"
    

class Gato(Animal):
    def __init__(self, nombre, vidas, marca_atun):
        super().__init__(nombre)
        self.vidas = vidas
        self.marca_atun = marca_atun

    def hacer_sonido(self):
        return "¡Miau!"

    def comer_atun(self):
        return f"{self.nombre} esta comiendo atún de la marca {self.marca_atun}"
        

mi_perro = Perro("Firulais")
print (mi_perro.nombre)
print (mi_perro. hacer_sonido())

mi_gato = Gato("Michi", 7, "Whiskas")
print(mi_gato.nombre)
print(mi_gato.hacer_sonido())
print(f"tiene {mi_gato.vidas} vidas")
print(mi_gato.comer_atun())

class Nadador:
    def nadar(self):
        return "Nadando"

class Volador:
    def volar(self):
        return "Volando"

class Pato(Nadador, Volador): 
    pass

pato = Pato()
print (pato.nadar () ) 
print (pato.volar ()) 

class Vehiculo:
    def arrancar(self):
        return "Motor encendido"

class CocheElectrico(Vehiculo):
    def arrancar(self):
        return "Batería activada"
        
auto = CocheElectrico()
print(auto.arrancar() )

class Persona:
    def __init__(self, nombre):
       self.nombre = nombre    

class Estudiante (Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre) 
        self.carrera = carrera

estudiante = Estudiante("Ana", "Ingeniería")
print (estudiante. nombre)
print(estudiante.carrera) 