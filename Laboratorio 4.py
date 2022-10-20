from cmath import cos

from distutils import core
 #El laboratorio 4
    #Se crea una lista con uno de los movimientos posibles
    #Se averigua cual es el numero mayor de estos
    #Pregunta si el nodo frontera es destinto de resultado
    #Se crea una list con posibles movimientos de el numero ingresado 
    #Posteriormente crea un nodo con esa lista de posibles movimientos 
    #Busca el ultimo numero o el numero mayor para saber cual movimiento esta ams cerca de su posicion
    #asigna un costo para saber cuanto de costo tomaria resolver por ese camino
    #Cuando el numero llega a su posicion se empieza a desglosar la rama 
    #Posteriormente aumenta el costo de los otros nodos para no ir por ese camino
    #Se pone un costo al nodo desglosado pàra saber la cantidad de movimientos 
    #asi este no aumente el costo del nodo padre como se hace en los demas nodos
    #se sabe del estado inicial , la solucion y se pone el costo en el nodo_solucion para imprimirlo
    #este costo es el resultado de sumar los costos padres del nodo desglosado 
# como ultimo aclarado se usa el sort para poder ordenar la lista y saber cuales serian las posibles combinaciones 
class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)
        
    def get_hijos(self):
        return self.hijos
    
    def set_padre(self, padre):
        self.padre = padre
        
    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def get_datos(self):
        return self.datos

    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self
                
    def set_costo(self, costo):
        self.costo = costo
        
    def get_costo(self):
        return self.costo
    
    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    
    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado
    
    def __str__(self):
        return str(self.get_datos())


def comparar_nodo(nodo):
    return nodo.get_costo()

def bpa(estado_inicio, estado_solucion, cantidad):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodo_inicio.set_costo(0)
    nodos_frontera.append(nodo_inicio)
    max = cantidad
    while resuelto == False and len(nodos_frontera) != 0:
        nodos_frontera = sorted(nodos_frontera, key = comparar_nodo, reverse = False)
        nodo_actual = nodos_frontera.pop(0)
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            for i in range(cantidad-1):
                hijo_datos = nodo_actual.get_datos().copy()
                temp = hijo_datos[i]
                hijo_datos[i] = hijo_datos[i+1]
                hijo_datos[i+1] = temp
                hijo = Nodo(hijo_datos)
                costo = 0
                for i in range(len(hijo_datos)):
                    if hijo_datos[i] == max:
                        costo = abs(hijo_datos[i] - (i+1))
                if costo == 0:
                    max -= 1
                    for nodo in nodos_frontera:
                        nodo.set_costo(nodo.get_costo() + cantidad)
                hijo.set_costo(costo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)
if __name__ == "__main__":
    num = int(input(" Numeros para ordenar: "))
    estado_inicial = list(range(num, 0, -1))
    solucion = list(reversed(estado_inicial))
    nodo_solucion = bpa(estado_inicial, solucion, num)
    costo = 0
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        costo += nodo_actual.get_costo()
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Costo del nodo: " + str(costo))