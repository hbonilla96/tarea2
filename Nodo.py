class Nodo:
    def __init__(self, valor=None, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def __str__(self):
        return "%s" % (self.valor)



