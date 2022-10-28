def torresdehanoi(n,o,d,aux):
    if( n>0):
        torresdehanoi(n-1,0,aux,d)
        print (" se mueve anillo desde torre " +str(o) +"hasta" + str (d))
        torresdehanoi(n-1,aux,d,o)
n = int(input("\n Favor ingresar cantidad de anillos "))
torresdehanoi(n,1,2,3)

     