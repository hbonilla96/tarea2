from aBinarios import aBinarios
from Nodo import Nodo

if __name__ == "__main__":
    ab = aBinarios()
    while (True):
        print("--Menú--\n" +
              "1. Agregar\n" +
              "2. Preorden\n" +
              "3.Postorden\n" +
              "4.Inorden\n")
        num = input("Ingrese la opción  ")
        if num == "1":
            valor = input("Ingrese el valor  ")
            nod = Nodo(valor)
            ab.agregar(nod)
        elif num == "2":
            print("Preorden")
            ab.preorden(ab.getRaiz())
        elif num == "3":
            print("Postorden")
            ab.postorden(ab.getRaiz())
        elif num == "4":
            print("Inorden")
            ab.inorden(ab.getRaiz())
