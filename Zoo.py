from Leon_ import Leon
from Oso_ import Oso
from Tigre_ import Tigre

class Zoo:
    
    def __init__(self, zoo_name):
        self.animales = []
        self.nombre = zoo_name
    def añadir_leon(self, name, edad):
        self.animales.append( Leon(name,edad) )
    def añadir_tigre(self, name, edad):
        self.animales.append( Tigre(name,edad) )
    def añadir_oso(self, name, edad):
        self.animales.append( Oso(name,edad) )
    def print_all_info(self):
        print("-"*30, self.nombre, "-"*30)
        for animal in self.animales:
            animal.mostrar_info()

zoo1 = Zoo("John's Zoo")
zoo1.añadir_leon("Nala",15)
zoo1.añadir_leon("Simba",10)
zoo1.añadir_leon("Rajah",8)
zoo1.añadir_tigre("Shere Khan",5)
zoo1.añadir_oso("Poo",7)
zoo1.print_all_info()

for animal in zoo1.animales:
    animal.alimentar()

zoo1.print_all_info()


