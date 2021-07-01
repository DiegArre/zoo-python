class Animal:
    def __init__(self,nombre,edad,salud,felicidad):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad
    
    def mostrar_info(self):
        print(f"""Nombre: {self.nombre}
        Edad: {self.edad}
        Salud: {self.salud}
        Felicidad: {self.felicidad}""")
        return self
    
    def alimentar(self,aumento = 10):
        self.felicidad += aumento
        self.salud += aumento
        return self

