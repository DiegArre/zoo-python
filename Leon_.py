from Animal_ import Animal

class Leon(Animal):
    def __init__(self, nombre, edad, pelaje = "Tipo1"):
        super().__init__(nombre, edad, 150, 50)
        self.colorpelaje = pelaje

    def alimentar (self):
        super().alimentar(15)
        return self

    def mostrar_info(self):
        super().mostrar_info()

# leon1 = Leon("leon1",15)

# leon1.mostrar_info()