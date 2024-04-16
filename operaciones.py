class Numero:
    """
    Clase base que representa un numero.
    """
    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        return self.valor

class Decorador(Numero):
    """
    Clase base para los decoradores que hereda de Numero
    """
    _numero = None

    def __init__(self, numero):
        self._numero = numero

    @property # Para que funcione como atributo
    def numero(self):
        return self._numero

    def mostrar(self):
        return self._numero.mostrar()

class SumarDos(Decorador):
    """
    Decorador que suma dos al valor del objeto Numero
    """
    def mostrar(self):
        return self.numero.mostrar() + 2

class MultiPorDos(Decorador):
    """
    Decorador que multiplica por dos al valor del objeto Numero
    """
    def mostrar(self):
        return self.numero.mostrar() * 2

class DivPorTres(Decorador):
    """
    Decorador que divide por tres al valor del objeto Numero
    """
    def mostrar(self):
        return self.numero.mostrar() / 3

# Ejemplo de uso
num = Numero(10)
print(num.mostrar())

sumados = SumarDos(num)
print(sumados.mostrar())

multipordos = MultiPorDos(sumados)
print(multipordos.mostrar())

divportres1 = DivPorTres(multipordos)
print(divportres1.mostrar())
