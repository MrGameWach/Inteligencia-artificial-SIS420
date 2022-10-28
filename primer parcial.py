from time import sleep

class vara:

    def __init__(self):
        #constructor inicializando pila "datopila"
        self.datopila = []
        #posicion de donde hay que insertar o eliminar un dato
        self.posicion=0

    def ordenar(self , x):
        self.datopila.insert(self.posicion,x)
        self.posicion=self.posicion+1

    def desordenar(self):
        try:
            self.posicion = self.posicion-1   
            copydatopila=self.datopila[self.posicion]
        #cuando se llama a desordenar este pone un 0 en la posicion en la que se encontraba
        # el anterior dato sacado  
            self.datopila[self.posicion]=0
            return copydatopila
        except:
            print("La vara esta vacia")
    
    #se declara vara vacia cuando no hay elementos en la pila , o vara donde van los discos
    def vara_vacia(self):
        #se retorna si la pila esta o no vacia 
        return self.datopila==[]
    
    def generar_disco(self,n):
        #Se crea el constructor vara para poder almacenar los discos o datos de la pila o vara 
        #en este caso
        varaf=[[]]
        copiar_n=n
        #Se representra la posicion 0 de la matriz donde "|" representa la vara
        #segun cuantos disco esten en esa vara 
        for i in range(2*n+3):
            if i==(2*n+3)//2:
                varaf[0].append('|')
            else:
                varaf[0].append(' ')
        #Dibuja los discos a la matriz con (--) un disco pequeño 
        for i in range(1,n+1):
            varaf.append([])
            for j in range(2*n+3):
                if j < copiar_n-1 or j>(2*i+copiar_n+1):
                    varaf[i].append(' ')
                elif j==copiar_n-1:
                    varaf[i].append('(')
                elif j==(2*i+copiar_n+1):
                    varaf[i].append(')')
                else:
                    varaf[i].append('-')
            copiar_n=1
            #retornara la vara con los discos que deberia dibujar 
        return varaf

    #recible torre 1 y torre 3 e invoca ala funcion pintar torre , se saca un dato de torre 1 
    # y se pone a la torre 3 y se da un tiempo para poder ver los pasos que hizo 
    def mover_disco(self,torre_1, torre_3):
        self.pintar_torres()
        dato=pilas[torre_1].desordenar()
        pilas[torre_3].ordenar(dato)
        print()
        sleep(1)


    def pintar_torres(self):
        
        for i in range(n,-1,-1):
            for j in range(3):
                self.gen_discos(pilas[j].datopila[i])
            print()
    
    def bpa(self,n,torre_1,torre_2,torre_3):
        if n==1:
            self.mover_disco(torre_1-1,torre_3-1)
        else:
            self.bpa(n-1,torre_1,torre_3,torre_2)
            #se llama ala funcion mover disco envez de imprimir directamente 
            self.mover_disco(torre_1-1,torre_3-1)
            self.bpa(n-1,torre_2,torre_1,torre_3)

    def gen_discos(self ,sin_discos):
        for i in varaf[sin_discos]:
            print(i,end="")

    def llenar_torre(self,n):
        #la pila se llena al revez de n hasta 0 c 
        for i in range(n,-1,-1):
            pilas[0].ordenar(i)
            pilas[1].ordenar(0)
            pilas[2].ordenar(0)
        
        pilas[0].posicion=n
        pilas[1].posicion= 0  
        pilas[2].posicion= 0

if __name__ == "__main__":
    v=vara()
    n=int(input("cantidad de discos= "))
    varaf= v.generar_disco(n)
    pilas=[vara(),vara(),vara()]
    v.llenar_torre(n)
    v.bpa(n,1,2,3)
    v.pintar_torres()
    


