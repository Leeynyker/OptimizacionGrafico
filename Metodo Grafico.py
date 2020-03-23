#Proyecto realizado por Andres Baquero y Leeynyker Montaño. 2020

123
from tkinter import *
import tkinter as tk 
import math
import numpy as np 
from matplotlib import pyplot as plt

#Clase donde se calculan los puntos de las rectas
class Calcular_Puntos(object):
    def __init__(self, x, y):
        #Atributos

        #Matriz que contiene los campos de texto de las inecuaciones
        self.__inecuaciones = x
        #El numero de inecuaciones
        self.__numIne = y
        #La matriz con valores de las inecuaciones
        self.__Valores = []
        #Lista que contiene los valores de X
        self.__X = list(range(self.__numIne))
        #Lista que contiene los valores de Y
        self.__Y = list(range(self.__numIne))
        #Lista que contiene los valores constantes
        self.__C = list(range(self.__numIne))
        #Lista que contiene los puntos cuando X=0
        self.__puntoX = list(range(self.__numIne))
        #Lista que contiene los puntos cuando Y=0
        self.__puntoY = list(range(self.__numIne))
        #Lista que contiene los puntos X a evaluar en la funcion objetivo
        self.__fX = list(range(self.__numIne))
        #Lista que contiene los puntos Y a evaluar en la funcion objetivo
        self.__fY = list(range(self.__numIne))
        #lista que contiene la pendiente de cada recta
        self.__m = list(range(self.__numIne))
        #Lista que contiene la constante de cada recta
        self.__b = list(range(self.__numIne))
        #Lista que guarda los valores reemplazados en la funcion
        self.__resul = list(range(self.__numIne))

        #Inicializando la matriz
        for i in range(self.__numIne):
            self.__Valores.append([])
            for j in range(4): 
                self.__Valores[i].append(None)

    #Metodo que calcula los puntos 
    def calcular(self):
        #Asignando los valores de las inecuaciones a la nueva matriz
        for i in range(self.__numIne):
            for j in range(4):
                self.__Valores[i][j] = self.__inecuaciones[i][j].get()
                if(j == 0):
                    self.__X[i] = int(self.__Valores[i][j])
                if(j == 1):
                    self.__Y[i] = int(self.__Valores[i][j])
                if(j == 3):
                    self.__C[i] = int(self.__Valores[i][j])

        #Despejando las variables X y Y
        for i in range(self.__numIne - 2):
            self.__puntoX[i] = self.__C[i]/self.__Y[i]
            self.__puntoY[i] = self.__C[i]/self.__X[i]

    #Metodo donde se grafican las rectas
    def graficar(self):
        a = range(-500,500)
        
        #Calcula la pendiente y la constante de la funcion
        for i in range(self.__numIne - 2):
            self.__m[i] = -self.__puntoY[i]/self.__puntoX[i]
            self.__b[i] = self.__puntoY[i]

        #Muestra la grafica
        plt.ion()

        #Area solución
        limX= 800
        for j in range(len(self.__puntoX)-2):
            print(self.__puntoX[j])
            if self.__puntoX[j] < limX:
                limX=self.__puntoX[j]
            print(limX)
        x_vals = np.linspace(0, limX,100)
        areaSol = []
        
        for i in range(self.__numIne  - 2):
            print(self.__Valores[i])
            if int(self.__Valores[i][0]) > 1:
                ptos=((int(self.__Valores[i][3]) - x_vals)/int(self.__Valores[i][0]))
            elif int(self.__Valores[i][1]) > 1:
                ptos=int(self.__Valores[i][3]) - x_vals*int(self.__Valores[i][1])
            else:
                ptos=int(self.__Valores[i][3])-x_vals
                
            
            areaSol.append(ptos)
        y_vals=areaSol[0]
        for i in range(self.__numIne  - 2):
            
            y_vals=np.minimum(y_vals,areaSol[i])
        
#        print(y_vals)

        
        
        #Grafica las funciones
        print(self.__puntoX)
        print(self.__puntoY)
        for i in range(self.__numIne  - 2):
            print(self.__Valores[i])
            def f(x):
                t = self.__m[i]*x + self.__b[i]
                #print(t)
                return self.__m[i]*x + self.__b[i]
            
            plt.plot(a, [f(i) for i in a])
            plt.xlim(0,400)
            plt.ylim(0,400)
        plt.fill_between(x_vals, y_vals, alpha=0.15, color='c')

    #Metodo en el cual se calcula la region factible de la funcion objetivo
    def region_factible(self):
        #Se calculan los puntos donde las rectas se intersectan
        for i in range(self.__numIne - 2):
            for j in range(self.__numIne - 2):
                if ((self.__m[i] - self.__m[j]) != 0):
                    y = (self.__b[j] - self.__b[i])/(self.__m[i] - self.__m[j])
                    if (self.__m[i]*y + self.__b[i] == self.__m[j]*y + self.__b[j]):
                        if (self.__m[i]*y + self.__b[i] >= 0) and (y >= 0):
                            self.__fX[i] = self.__m[i]*y + self.__b[i]
                            self.__fY[i] = y
                        else:
                            self.__fX[i] = 0
                            self.__fY[i] = 0

        #Se obtienen los datos de la funcion objetivo
        funcX = int(fObj1.get())
        funcY = int(fObj2.get())
        fMax_Min = fObj3.get()

        #Se calculan todos los valores que tiene la funcion objetivo con los diferentes puntos
        for i in range(self.__numIne - 2):
            self.__resul[i] = funcX*self.__fX[i] + funcY*self.__fY[i]

        #Se calcula el maximo en caso de que se pida
        if fMax_Min == 'max':
            num = 0
            for i in range(self.__numIne - 2):
                if num < self.__resul[i]:
                    num = self.__resul[i]
                    texto = "Valor máximo: " + str(num) + "    (x = " + str(self.__fX[i])+", y = "+str(self.__fY[i])+")"
            lbl6.config(text = texto)
        #Se calcula el minimo en caso de que se pida
        else:
            num = 99999
            for i in range(self.__numIne - 2):
                if num > self.__resul[i]:
                    num = self.__resul[i]
                    texto = "Valor mínimo: " + str(num) + "    (x = " + str(self.__fX[i]) + ", y = " + str(self.__fY[i]) + ")"
            lbl6.config(text = texto)

#Clase donde se crean los campos para las inecuaciones
class Inecuaciones(Calcular_Puntos):
    def __init__(self, x):
        #Atributos

        #El numero de inecuaciones
        self.__numIne = int(x)
        #Matriz donde se guardan los campos de las inecuaciones
        self.__Inecuaciones = []
        self.__CalcularPuntos = None

        #Inicializando la matriz
        for i in range(self.__numIne):
            self.__Inecuaciones.append([])
            for j in range(4): 
                self.__Inecuaciones[i].append(None)

    def iniciar(self):
        #Creando los campos para las inecuaciones
        for i in range(self.__numIne):
            for j in range(4):
                self.__Inecuaciones[i][j] = tk.Entry(marco, width = 7)
                self.__Inecuaciones[i][j].pack()
                self.__Inecuaciones[i][j].place(x = j*100 + 100, y = i*30 + 150)

                if j == 2:
                    if i >= self.__numIne - 2:
                        self.__Inecuaciones[i][j].insert(0, ">=")
                        self.__Inecuaciones[i][j].config(state = "readonly")
                    else:
                        self.__Inecuaciones[i][j].insert(0, "<=")

        #Se muestran las inecuaciones de positividad de las variables
        self.__Inecuaciones[self.__numIne - 2][0].insert(0, "1")
        self.__Inecuaciones[self.__numIne - 2][0].config(state = "readonly")
        self.__Inecuaciones[self.__numIne - 2][1].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 2][1].config(state = "readonly")
        self.__Inecuaciones[self.__numIne - 2][3].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 2][3].config(state = "readonly")

        self.__Inecuaciones[self.__numIne - 1][0].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 1][0].config(state = "readonly")
        self.__Inecuaciones[self.__numIne - 1][1].insert(0, "1")
        self.__Inecuaciones[self.__numIne - 1][1].config(state = "readonly")
        self.__Inecuaciones[self.__numIne - 1][3].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 1][3].config(state = "readonly")

    def hacer_algo(self):
        #Llamando a la clase Calcular_Puntos
        Calcular_Puntos.__init__(self, self.__Inecuaciones, self.__numIne)
        Calcular_Puntos.calcular(self)
        Calcular_Puntos.graficar(self)
        Calcular_Puntos.region_factible(self)

#Funcion para llamar a la clase Inecuaciones
def calc_ine():
    objeto = Inecuaciones(numIne.get())
    objeto.iniciar()

    #Boton para enviar inecuaciones
    btnCalcular = Button(marco, text ="Calcular", command = objeto.hacer_algo, width = 10)
    btnCalcular.pack()
    btnCalcular.place(x = 500, y = 200)

#Crea el marco
marco = tk.Tk()
marco.title("Maximizar - Metodo Grafico")
marco.geometry("600x400")
marco.configure(background="#ffffff")

#Etiquetas
lbl1 = tk.Label(marco, text = "Función objetivo: ")
lbl1.pack()
lbl1.place(x = 0, y = 30)

lbl2 = tk.Label(marco, text = "X      +")
lbl2.pack()
lbl2.place(x = 230, y = 30)

lbl3 = tk.Label(marco, text = "Y")
lbl3.pack()
lbl3.place(x = 380, y = 30)

lbl4 = tk.Label(marco, text = "max o min")
lbl4.pack()
lbl4.place(x = 530, y = 30)

lbl5 = tk.Label(marco, text = "Digite el numero de inecuaciones: ")
lbl5.pack()
lbl5.place(x = 0, y = 90)

lbl6 = tk.Label(marco, text = "")
lbl6.pack()
lbl6.place(x = 200, y = 350)

lbl7 = tk.Label(marco, text = "Coef X")
lbl7.pack()
lbl7.place(x = 100, y = 120)

lbl8 = tk.Label(marco, text = "Coef Y")
lbl8.pack()
lbl8.place(x = 200, y = 120)

#Funcion objetivo
fObj1 = tk.Entry(marco, width = 10)
fObj1.pack(anchor = CENTER)
fObj1.place(x = 150, y = 30)

fObj2 = tk.Entry(marco, width = 10)
fObj2.pack(anchor = CENTER)
fObj2.place(x = 300, y = 30)

fObj3 = tk.Entry(marco, width = 10)
fObj3.pack(anchor = CENTER)
fObj3.place(x = 450, y = 30)

#Inecuaciones
numIne = tk.Entry(marco, width = 10)
numIne.pack(anchor = CENTER)
numIne.place(x = 200, y = 90)

#Boton enviar inecuaciones
btnEnviar = tk.Button(marco, text ="Enviar", command = calc_ine, width = 10)
btnEnviar.pack()
btnEnviar.place(x = 350, y = 90)

marco.mainloop()
