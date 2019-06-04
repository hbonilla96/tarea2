import Nodo

class aBinarios:
    def __init__(self):
        self.raiz = None

    def agregar(self, elemento):
        if self.raiz == None:
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.valor) >= int(aux.valor):
                    aux = aux.der
                else:
                    aux = aux.izq
            if int(elemento.valor) >= int(padre.valor):
                padre.der = elemento
            else:
                padre.izq = elemento

    def preorden(self, elemento):
        if elemento != None:
            print(elemento)
            self.preorden(elemento.izq)
            self.preorden(elemento.der)

    def postorden(self, elemento):
        if elemento != None:
            self.postorden(elemento.izq)
            self.postorden(elemento.der)
            print(elemento)

    def inorden(self, elemento):
        if elemento != None:
            self.inorden(elemento.izq)
            print(elemento)
            self.inorden(elemento.der)

    def getRaiz(self):
        return self.raiz