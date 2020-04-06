#Proyecto realizado por Andres Baquero y Leeynyker Montaño. 2020

from tkinter import *
import tkinter as tk 
import math
import numpy as np 
from matplotlib import pyplot as plt


#Clase para describir cada punto
class punto:
  def __init__(self,x,y):
    self.px = x
    self.py = y
  def __str__(self):
    return "("+str(self.px)+","+str(self.py)+")"

#Halla interseccion entre dos rectas
class linea:
  def __init__(self, p0, p1):
    self.p0 = p0
    self.p1 = p1
    self.A = p1.px - p0.px
    self.B = p1.py - p0.py
    self.C = p1.px*p0.py - p0.px*p1.py
  def intersecta(self, otro):
    det = self.A*otro.B - otro.A*self.B
    cx = otro.A*self.C-self.A*otro.C
    cy = otro.B*self.C-self.B*otro.C
    if det != 0:
        cordenadas=[cx/det,cy/det]
    else:
        cordenadas=[0,0]
    return (cordenadas) #Devuelve las cordenadas de los puntos de interseccion entre las rectas


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

        self.__area = list(range(self.__numIne-2))
        self.__q = 0
        self.__areaOrd = list(range(self.__numIne-2))
        self.__lista = list(range(self.__numIne-2))
        #Lista que contiene los valores de X
        self.__X = list(range(self.__numIne))
        #Lista que contiene los valores de Y
        self.__Y = list(range(self.__numIne))
        #Lista que contiene los valores constantes
        self.__C = list(range(self.__numIne))
        #Lista que contiene el signo de la inecuacion
        self.__signo = list(range(self.__numIne))
        #Lista que contiene los puntos cuando X=0
        self.__puntoX = list(range(self.__numIne-2))
        #Lista que contiene los puntos cuando Y=0
        self.__puntoY = list(range(self.__numIne-2))
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
        
        self.__estado = list(range(self.__numIne))

        self.__a = 0

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
                if(j == 2):
                    self.__signo[i] = self.__Valores[i][j]
                if(j == 3):
                    self.__C[i] = int(self.__Valores[i][j])

        #Despejando las variables X y Y
        for i in range(self.__numIne - 2):
            if self.__Y[i] > 0 or self.__Y[i] < 0:
                self.__puntoX[i] = self.__C[i]/self.__Y[i] #Cuando X = 0

            else:
                self.__puntoX[i] = 0 #Cuando X = 0


            if self.__X[i] > 0 or self.__X[i] < 0:
                self.__puntoY[i] = self.__C[i]/self.__X[i] #Cuando Y = 0

            else:
                self.__puntoY[i] = 0 #Cuando Y = 0
             

            self.__area[i] = abs(self.__puntoX[i]*self.__puntoY[i]/2)

        #self.__puntoX tiene los puntos de corte con el eje X
        #self.__puntoY tiene los puntos de corte con el eje Y
        
        for i in range(self.__numIne - 2):
            if(self.__signo[i] == '>='):
                self.__estado[i] = 1
            else:
                self.__estado[i] = 0

        self.__areaOrd = sorted(self.__area)
        for i in range(self.__numIne-2):
            if(self.__areaOrd[0] == self.__area[i]):
                self.__q = i
                
    #Metodo donde se grafican las rectas
    def graficar(self):
        a = range(-500,500)
        
        #Calcula la pendiente y la constante de la funcion
        for i in range(self.__numIne - 2):
            if(self.__puntoY[i] != 0):
                self.__m[i] = -self.__puntoX[i]/self.__puntoY[i]
                self.__b[i] = self.__puntoX[i]
            else:
                self.__m[i] = 0
                self.__b[i] = self.__puntoX[i]

        #Muestra la grafica
        plt.ion()

        #Area solución
        
        x_vals = np.linspace(0, 400,100)#area a colorear en x
        

        #Colorea El area de soluciones posibles - falta hacer arreglos
        for i in range(self.__numIne  - 2):
            
            areaSol = [] #Almacena area solucion de la recta (puntos de la desigualdad)
            areaSoli = []#Almacena punto de inicio del area solucion(desde donde van los puntos de la desigualdad)
       
        
            ptosf=0
            ptosi=0
            
            #Hallar el area solución de cada recta 
                #Analizando cada recta, sus puntos de corte y la desigualdad <= o >=
            if int(self.__Valores[i][0]) > 0 and int(self.__Valores[i][1]) > 0 :
                if self.__Valores[i][2] == "<=":
                    ptosf=((int(self.__Valores[i][3]) - x_vals*int(self.__Valores[i][0]))/int(self.__Valores[i][1]))
                    ptosi=0
                else:
                    ptosf=800
                    ptosi=((int(self.__Valores[i][3]) - x_vals*int(self.__Valores[i][0]))/int(self.__Valores[i][1]))
            elif int(self.__Valores[i][0]) == 0 and int(self.__Valores[i][1]) > 0 :
                if self.__Valores[i][2] == "<=":
                    ptosf=(int(self.__Valores[i][3]) - 0)/int(self.__Valores[i][1])
                    ptosi=0
                else:
                    ptosf=800
                    ptosi=(int(self.__Valores[i][3]) - 0)/int(self.__Valores[i][1])
            elif int(self.__Valores[i][0]) > 0 and int(self.__Valores[i][1]) == 0 :
                if self.__Valores[i][2] == "<=":
                    ptosf=((int(self.__Valores[i][3]) - x_vals*int(self.__Valores[i][0])))/0.0000001
                    ptosi=0
                else:
                    ptosf=800
                    ptosi=((int(self.__Valores[i][3]) - x_vals*int(self.__Valores[i][0])))/0.0000001
            else:
                if self.__Valores[i][2] == "<=":
                    ptosf=int(self.__Valores[i][3])-x_vals
                    ptosi=0
                else:
                    ptosf=800
                    ptosi=int(self.__Valores[i][3])-x_vals
                    
                
            areaSol.append(ptosf)
            areaSoli.append(ptosi)
            
            
            
            y_vals=areaSol[0]
            y_vali=areaSoli[0]
            
            #Colorea el area seleccionda teniendo encuenta la desigualdad
            if self.__Valores[i][2] == "<=":
                plt.fill_between(x_vals,0, y_vals,interpolate=True, alpha=0.15, color='b')
            else:
                plt.fill_between(x_vals,y_vali, 800,interpolate=True, alpha=0.15, color='b')


        #Grafica las funciones
        def y(x):
            return 0
        plt.plot(a, [y(i) for i in a], 'k')
        plt.plot([y(i) for i in a], a, 'k')

        i = 0
        c = 0
        while c != 1:
            if(self.__Y[i] == 0):
                def h(x):
                    return self.__C[i]/self.__X[i]

                plt.plot([h(i) for i in a], a)
                if(i == self.__numIne - 2):
                    c = 1
            else:
                if(i == self.__numIne - 2):
                    c = 1
            i = i+1
            


        for i in range(self.__numIne  - 2):
            def f(x):
                t = self.__m[i]*x + self.__b[i]
                #print(t)
                return self.__m[i]*x + self.__b[i]

            plt.plot(a, [f(i) for i in a])
            
            plt.xlim(0,400)
            plt.ylim(0,400)
        
        
        plt.xlim(0,400)
        plt.ylim(0,400)
        
        

    #Metodo en el cual se calcula la region factible de la funcion objetivo
    def region_factible(self):
        
        flag = False #bandera de casos
        infinit=0 
        zerox=0
        
        #cuenta si todas las ecuaciones tienen la misma desigualdad >= o <=
        for i in range(self.__numIne  - 2):
            if self.__Valores[i][2] == "<=":
                zerox=zerox+1
            else:
                infinit=infinit+1
                
        #Analiza si la solucion es 0 o infinito
        metod = fObj3.get()
        if metod == "max" and infinit == (self.__numIne  - 2):
            flag = True
            texto = "Es infinito"
        elif metod == "min" and zerox == (self.__numIne  - 2):
            flag = True
            texto =  "Valor minimo: 0    (x = 0 , y = 0)"
        else:
            flag = False
       
        
        #Si la bandera se mantiene en falso analiza los puntos de interseccion y corte
        #Para hallar la solucion
        if flag == False:
            
            d=0
            z=0
            intersex=[]#Almacena los puntos de interseccion entre las rectas 
            while  d < self.__numIne - 2:
                
                if d < (self.__numIne-2)-1 :
                    z = d+1
                else:
                    
                    z= 0
                
                
                ptx1=self.__puntoY[d]
                ptx2=self.__puntoY[z]
                
                pty1=self.__puntoX[d]
                pty2=self.__puntoX[z]
                    
            #Analiza los puntos de interseccion entre todas as rectas
                if ptx1 > 0 and pty1 > 0:            
                    L1 =linea(punto(ptx1,0),punto(0,pty1))
                elif ptx1 > 0 and pty1 == 0:
                    L1 =linea(punto(ptx1,0),punto(ptx1,0.1))
                elif ptx1 == 0 and pty1 > 0:
                    L1 =linea(punto(0.1,pty1),punto(0,pty1))
                    
                if ptx2 > 0 and pty2 > 0:            
                    L2 =linea(punto(ptx2,0),punto(0,pty2))
                elif ptx2 > 0 and pty2 == 0:
                    L2 =linea(punto(ptx2,0),punto(ptx2,0.1))
                elif ptx2 == 0 and pty2 > 0:
                    L2 =linea(punto(0.1,pty2),punto(0,pty2))
                    
                
                
                intersex.append(L1.intersecta(L2))#Puntos de interseccíon
                
                d = d+1
            #Agrega puntos de corte de las rectas con los ees X y Y  a el conjunto de intersecciones
            for i in range(len(self.__puntoY)):
                intersex.append([self.__puntoY[i],0])
            for j in range(len(self.__puntoX)):
                intersex.append([0,self.__puntoX[j]])
                

            
            
            factibles=[] #puntos factibles de solucion
            infact=[] #puntos que no pueden ser parte de la solución
            
            #analizamos que puntos pueden hacer parte de la solución 
            for i in range(self.__numIne  - 2):
                for n in range(len(intersex)):
                    valor = int(self.__Valores[i][0])*intersex[n][0] +  int(self.__Valores[i][1])*intersex[n][1]
                    if valor != 0:
                        
                        if self.__Valores[i][2] == "<=":
                            if valor <= float(self.__Valores[i][3]):
                                factibles.append(intersex[n])
                            else:
                                infact.append(intersex[n])
                        else:
                           
                            if valor >= float(self.__Valores[i][3]):
                                factibles.append(intersex[n])
                            else:
                                infact.append(intersex[n])
        
            
            salto=len(intersex)
            
            #Elimina los valores que no pueden ser posibles del grupo de intersecciones y cortes 
            for i in range(salto):
                for j in range(len(infact)):
                    if intersex[i] == infact[j]:
                        intersex[i]=[0,0]
                        salto=len(intersex)
                        
    
                                   
    
            #Se obtienen los datos de la funcion objetivo
            funcX = int(fObj1.get())
            funcY = int(fObj2.get())
            fMax_Min = fObj3.get()
            
            posibles=[] #Valores posibles de solucion
            poxi=[] #Pocision de los valores posibles en la lista
            
            #Analizar cada punto del conjunto intersecciones en las desigualdades
            
            for i in range(len(intersex)):
                if intersex[i][0] == 0 and intersex[i][1] == 0:
                    print("")
                else:
                    obs = funcX*intersex[i][0] + funcY*intersex[i][1]
                    
                    posibles.append(obs)
                    poxi.append(i)
                    
            
            #Analiza si hay soluciones posibles 
            if len(posibles) > 0:
                #Si el problema es de maximización obtiene el valor mayor 
                if fMax_Min == "max":
                    num_max=max(posibles)
                    
                    pos_max=posibles.index(max(posibles))
                    pval = poxi[pos_max]
                    
                    #
                    texto = "Valor máximo: " + str(num_max) + "    (x = " + str(intersex[pval][0])+", y = "+str(intersex[pval][1])+")"
                #Si el problema es de minnimización obtiene el valor menor
                else:
                    num_min=min(posibles)
                    pos_min=posibles.index(min(posibles))
                    pval = poxi[pos_min]
                    
                    texto = "Valor minimo: " + str(num_min) + "    (x = " + str(intersex[pval][0])+", y = "+str(intersex[pval][1])+")"
            
            else:
                texto="No tiene solución"
        
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
marco.configure(background="#5DA0FF")

#Etiquetas
lbl1 = tk.Label(marco, text = "Función objetivo: ")
lbl1.pack()
lbl1.configure(background="#5DA0FF")
lbl1.place(x = 0, y = 30)

lbl2 = tk.Label(marco, text = "X      +")
lbl2.pack()
lbl2.configure(background="#5DA0FF")
lbl2.place(x = 230, y = 30)

lbl3 = tk.Label(marco, text = "Y")
lbl3.pack()
lbl3.configure(background="#5DA0FF")
lbl3.place(x = 380, y = 30)

lbl4 = tk.Label(marco, text = "max o min")
lbl4.pack()
lbl4.configure(background="#5DA0FF")
lbl4.place(x = 530, y = 30)

lbl5 = tk.Label(marco, text = "Digite el numero de inecuaciones: ")
lbl5.pack()
lbl5.configure(background="#5DA0FF")
lbl5.place(x = 0, y = 90)

lbl6 = tk.Label(marco, text = "")
lbl6.pack()
lbl6.configure(background="#5DA0FF")
lbl6.place(x = 100, y = 350)

lbl7 = tk.Label(marco, text = "Coef X")
lbl7.pack()
lbl7.configure(background="#5DA0FF")
lbl7.place(x = 100, y = 120)

lbl8 = tk.Label(marco, text = "Coef Y")
lbl8.pack()
lbl8.configure(background="#5DA0FF")
lbl8.place(x = 200, y = 120)

#Funcion objetivo
fObj1 = tk.Entry(marco, width = 10)
fObj1.pack(anchor = CENTER)
fObj1.config(background="#CDF0FE")
fObj1.place(x = 150, y = 30)

fObj2 = tk.Entry(marco, width = 10)
fObj2.pack(anchor = CENTER)
fObj2.config(background="#CDF0FE")
fObj2.place(x = 300, y = 30)

fObj3 = tk.Entry(marco, width = 10)
fObj3.pack(anchor = CENTER)
fObj3.config(background="#CDF0FE")
fObj3.place(x = 450, y = 30)

#Inecuaciones
numIne = tk.Entry(marco, width = 10)
numIne.pack(anchor = CENTER)
numIne.config(background="#6CD5FF")
numIne.place(x = 200, y = 90)

#Boton enviar inecuaciones
btnEnviar = tk.Button(marco, text ="Enviar", command = calc_ine, width = 10)
btnEnviar.pack()
btnEnviar.place(x = 350, y = 90)

marco.mainloop()
