import re
import numpy as np
import math
import matplotlib.pyplot as plt

def getcoef():  # recuerda que si no hay termino independiente se le quita el espacio al final de la funcion
    read_coef = open("C:\\Archivos\\coeficientes.txt", "r", encoding="utf-8")
    get_coef = read_coef.read()
    read_coef.close()

    temp = re.findall(r'(-?\d*)x', get_coef) + re.findall(r'(-?\d*) ', get_coef)  # toma los coeficientes
    pot = ("".join(re.findall(r'(\^\d*)', get_coef))).split("^")  # toma las potencias

    # arreglamos temp con espacio
    for i in range(len(temp)):
        if temp[i] == '':
            temp[i] = 1
        elif temp[i] == '-':
            temp[i] == -1
    potx = re.findall(r'(x\^)', get_coef)
    pot1 = re.findall(r'(x\d*)', get_coef)

    global coeficientes

    del pot[0]  # borra un lugar de la lista ocupado por un espacio en blanco
    potencias = list(map(int, pot))  # convierte la lista de strings de potencias en lista de ints
    coeficientes = list(map(int, temp))  # convierte la lista de strings de coeficientes en lista de ints

    bandera = False
    if len(pot1) != len(potx):  # agarrar la potencia 1 dek valro x      pot1 numero de x, potx numero de x con un ^
        potencias.append(1)
    # si el numero de x y de x^ es igual y el numero de coef es mayor al de potencias
    elif len(pot1) == len(potx) and len(coeficientes) > len(potx) > 1:
        potencias.append(0)
    elif len(pot1) == len(potx) and len(potx) == 1:
        print("es una unica x ")
        bandera = True  # if True es ua sola x y puede (o no) contener algun otro termino

    # def Dic
    # armamos el dicionario que relaciona coef y potencias
    global DicCoefPow
    if len(potencias) == len(coeficientes):
        DicCoefPow = dict(zip(potencias, coeficientes))
    else:
        potencias.append(0)  # agrego un 0 para len(potencias) == len(coeficientes) y que sea posible armar el
        # diccionario
        DicCoefPow = dict(zip(potencias, coeficientes))
        potencias.remove(0)  # quito el cero que agregue arriba para que la variable potencias solo tengapotencias
        # necesaria
    global grado
    potencias.sort()
    potencias.reverse()
    grado = potencias[0]

    # def FixPotencias
    # Arregla las potencias ////////////////////////////////(fixpow)
    fixpow = []
    for cont in range(grado + 1):
        fixpow.append(cont)
    fixpow.reverse()

    # def fixcoef
    # Arregla los coeficientes /////////////////////////////(fixcoef)
    fixcoef = []
    for i in range(grado + 1):
        if DicCoefPow.get(i) in coeficientes:
            fixcoef.append(DicCoefPow.get(i))
        else:
            fixcoef.append(0)
    fixcoef.reverse()
    return fixcoef


def LongitudArco(f, a, b):# f=funcion,a=intSUP, b+intIF, n=numero de x
    n = 10000
    df = f.deriv(1) #sacamos la primera derivada
    #la = np.poly1d(math.sqrt(1+pow(df(2), 2)))

    h = (b - a)/n # h = numero de subintervalos
    suma = 0.0
    for i in range(1, n):
        #calculamos x
        x = a + i * h
        if (i % 2 == 0): # si x es par
            suma = suma + 2 * math.sqrt(1+pow(df(x), 2))    #   se multiplica por 4
        else:
            suma = suma + 4 * math.sqrt(1+pow(df(x), 2))    #   se multiplica por 2
    suma = suma + math.sqrt(1+pow(df(a), 2)) + math.sqrt(1+pow(df(b), 2))    #   sumamos el primer elemento y el ultimo
    resp = suma * (h/ 3)
    return resp


if __name__ == '__main__':  # función main
    f = np.poly1d(getcoef())
    print(f)
    a =  int(input("cual es el limite inferior?"))
    b =  int(input("cual es el limite superior?"))
    print(LongitudArco(f, a, b))

    t = np.arange(0.0,3.0,0.01)
    s = 1 + np.sin(2 * np.pi * t)
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.grid()

    plt.show()