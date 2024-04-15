from abc import ABC, abstractmethod

class Laminador:
    """
    Clase abstracta que define la interfaz para todas las implementaciones concretas.
    """
    @abstractmethod
    def producir(self, lamina):
        pass
    
class Laminador5Mts(Laminador):
    """
    Clase que implementa la interfaz de Laminador para un laminador de 5 metros.
    """
    def producir(self, lamina):
        return f"Produciendo lámina de {lamina.espesor}\" de espesor y {lamina.ancho} mts de ancho en laminador de 5 mts"
    
class Laminador10Mts(Laminador):
    """
    Clase que implementa la interfaz de Laminador para un laminador de 10 metros.
    """
    def producir(self, lamina):
        return f"Produciendo lámina de {lamina.espesor}\" de espesor y {lamina.ancho} mts de ancho en laminador de 10 mts"
    
class Lamina:
    """
    Clase que representa una lámina de acero. Esta es la abstracción en el patrón Bridge.
    """
    def __init__(self, espesor, ancho, laminador):
        self.espesor = espesor
        self.ancho = ancho
        self.laminador = laminador
        
    def producir(self):
        return self.laminador.producir(self)

# Ejemplo de uso
lamina1= Lamina(0.5, 1.5, Laminador5Mts())
print(lamina1.producir())

lamina2 = Lamina(0.5, 1.5, Laminador10Mts())
print(lamina2.producir())