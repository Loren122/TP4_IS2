class Componente:
    def __init__(self, nombre):
        self.nombre = nombre

    def agregar(self, componente):
        pass

    def mostrar(self, profundidad=0):
        print('-' * profundidad + self.nombre)

class Pieza(Componente):
    pass

class ComponenteCompuesto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, profundidad=0):
        print('-' * profundidad + self.nombre)
        for componente in self.componentes:
            componente.mostrar(profundidad + 2)

# Crear el producto principal
producto_principal = ComponenteCompuesto('Producto Principal')

# Crear los tres subconjuntos
for i in range(1, 4):
    subconjunto = ComponenteCompuesto(f'Subconjunto {i}')
    producto_principal.agregar(subconjunto)

    # Agregar cuatro piezas a cada subconjunto
    for j in range(1, 5):
        pieza = Pieza(f'Pieza {j} de Subconjunto {i}')
        subconjunto.agregar(pieza)

# Mostrar la configuración
producto_principal.mostrar()

# Crear y agregar un subconjunto opcional
subconjunto_opcional = ComponenteCompuesto('Subconjunto Opcional')
for i in range(1, 5):
    pieza = Pieza(f'Pieza {i} de Subconjunto Opcional')
    subconjunto_opcional.agregar(pieza)

producto_principal.agregar(subconjunto_opcional)

# Mostrar la configuración con el subconjunto opcional
print("\nCon Subconjunto Opcional:\n")
producto_principal.mostrar()
