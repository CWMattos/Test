import sys
from paquete.funciones_matematicas import multiplicar
import pandas as pd




if len(sys.argv) == 3:
    nombre= sys.argv[1]
    cantidad= int(sys.argv[2])
    
    for i in range(multiplicar(cantidad,2)):
        print("hola",nombre)
else:
    print("Atencion, argumentos incorrectos, espera 2 argumentos!")

