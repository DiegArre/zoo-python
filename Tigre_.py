from Animal_ import Animal

class Tigre(Animal):
    def __init__(self,nombre,edad, manchas = True):
        super().__init__(nombre, edad, 100, 80)
        self.manchas = manchas

    def alimentar (self):
        super().alimentar(13)
        return self

    def mostrar_info(self):
        super().mostrar_info()

# tigre = Tigre("leon1",15)

# tigre.mostrar_info()