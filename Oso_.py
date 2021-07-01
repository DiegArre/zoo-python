from Animal_ import Animal

class Oso(Animal):
    def __init__(self,nombre,edad,peso = 100):
        super().__init__(nombre, edad, 200, 100)
        self.peso = peso

    def alimentar (self):
        super().alimentar(8)
        return self

    def mostrar_info(self):
        super().mostrar_info()

# oso1 = Oso("oso",15)

# oso1.mostrar_info()