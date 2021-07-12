import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QLCDNumber
from PyQt5.uic import loadUi
from prix2 import Ui_segunda
import listas
from prix import Ui_v10
from listas import *
import fun
import listas
import matplotlib.pyplot as plt
import pandas as pd
from pandastable import Table, TableModel

import tkinter as tk
import numpy as np
import math

qtCreatorFile = "prix.ui" # Nombre del archivo aquí.
tipo_instalaciones = []
condiciones = []
tipo_sustancia = []
tipo_sus_t_i_e=[]
cantidad_sustancia = []
distancias_s = []
o1=[]
o2=[]
o3_t=[]
o3_i=[]
o3_e=[]
g=[]
d=[]
A_tox=[]
A_inf=[]
A_exp=[]
num_ins=[]
dis_=[]
s1t=[]
s2e=[]
s3i=[]
distancias_=[]
dis_a=[]
select=[]
contador=[]
contador__=[]
mm=1   
number=1
numero_ubicaciones=0
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('prix.ui', self)
        self.boton1.clicked.connect(self.abrirsegunda)
        self.boton2.clicked.connect(self.salir_prin)



    def abrirsegunda(self):
        self.hide()
        otraventana=Cargar_datos(self)
        otraventana.show()


    def salir_prin(self):
        self.parent()
        self.close()

class DataFrameTable(tk.Frame):
    def __init__(self, parent=None, df=pd.DataFrame()):
        super().__init__()
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.table = Table(
            self, dataframe=df,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)
        self.table.show()
class Cargar_datos(QMainWindow):
 
    def __init__(self,parent=None):
        super(Cargar_datos, self).__init__(parent)
        loadUi('prix2.ui', self)
        self.pushButton_4.clicked.connect(self.Salir)
        self.pushButton11.clicked.connect(self.Guardar)
        self.pushButton11.clicked.connect(self.limpiardatos)
        self.pushButton_3.clicked.connect(self.Guardar)
        self.pushButton_3.clicked.connect(self.Tabla)
        self.pushButton_3.clicked.connect(self.cerrar)
        self.pushButton_11.clicked.connect(self.abrirayuda)
        self.B3.clicked.connect(self.abri_anadir)
        self.lcd.display(number)


    def abri_anadir(self):
        self.hide()
        anadir=Anadir(self)
        anadir.show()
    def abrirayuda(self):
        self.hide()
        otraventana=Ventanaayuda(self)
        otraventana.show()
    def cerrar(self):
        self.parent().show()
        self.close()
    def limpiardatos(self):
        self.parent().show()
        self.close()
        self.hide()
        otraventana = Cargar_datos(self)
        otraventana.show()

    def Tabla(self):


        print(contador)
        k = 0
        for i in (contador):
            if contador[i] == 0:
                k = k + 1
                pass

            elif contador[i] == 1:
                contador__.append(k)
            else:
                pass
        for i in range(len(s1t)):
            g=0
            s=str()
            if s1t[i]>g:
                g=s1t[i]
                s="s1"
            if s2e[i]>g:
                s="s2"
                g=s2e[i]
            if s3i[i]>g:
                s="s3"
                g=s3i[i]
            select.append(s)
        lista_general = [contador__, distancias_s, s1t, s2e, s3i,select]
        df_general = pd.DataFrame(lista_general, index=['Instalación', 'distancias', 'stox', 'sexp', 'sinf','selected']).transpose()
        df = df_general
        #listas para almacenar
        d1 = []
        d2 = []
        d3 = []
        d4 = []
        d5 = []
        d6 = []
        d7 = []
        d8 = []
        s1to=[]
        s1ex=[]
        s1in=[]
        s2to = []
        s2ex = []
        s2in = []
        s3to = []
        s3ex = []
        s3in = []
        s4to = []
        s4ex = []
        s4in = []
        s5to = []
        s5ex = []
        s5in = []
        s6to = []
        s6ex = []
        s6in = []
        s7to = []
        s7ex = []
        s7in = []
        s8to = []
        s8ex = []
        s8in = []
        

        for i in range(len(contador__)):
            if contador__[i]==1:
                s1to.append(s1t[i])
                s1ex.append(s2e[i])
                s1in.append(s3i[i])
                d1.append(distancias_s[i])
            if contador__[i]==2:
                s2to.append(s1t[i])
                s2ex.append(s2e[i])
                s2in.append(s3i[i])
                d2.append(distancias_s[i])
            if contador__[i]==3:
                s3to.append(s1t[i])
                s3ex.append(s2e[i])
                s3in.append(s3i[i])
                d3.append(distancias_s[i])
            if contador__[i]==4:
                s4to.append(s1t[i])
                s4ex.append(s2e[i])
                s4in.append(s3i[i])
                d4.append(distancias_s[i])
            if contador__[i]==5:
                s5to.append(s1t[i])
                s5ex.append(s2e[i])
                s5in.append(s3i[i])
                d5.append(distancias_s[i])
            if contador__[i]==6:
                s6to.append(s1t[i])
                s6ex.append(s2e[i])
                s6in.append(s3i[i])
                d6.append(distancias_s[i])
            if contador__[i]==7:
                s7to.append(s1t[i])
                s7ex.append(s2e[i])
                s7in.append(s3i[i])
                d7.append(distancias_s[i])
            if contador__[i]==8:
                s8to.append(s1t[i])
                s8ex.append(s2e[i])
                s8in.append(s3i[i])
                d8.append(distancias_s[i])
       # segundo dataframe

        num_ub=int(numero_ubicaciones/contador__[-1])
        df1 = pd.DataFrame(columns=[],index=range(num_ub))  
        if len(d1)>0:
            df1=df1.assign(distancias_i1=d1)
        
        if len(d2)>0:
            df1=df1.assign(distancias_i2=d2)
        
        if len(d3)>0:
            df1 = df1.assign(distancias_i3=d3)
        
        if len(d4)>0:
            df1 = df1.assign(distancias_i4=d4)
        
        if len(d5)>0:
            df1 = df1.assign(distancias_i5=d5)
        
        if len(d6)>0:
            df1 = df1.assign(distancias_i6=d6)
        
        if len(d7)>0:
            df1 = df1.assign(distancias_i7=d7)
        
        if len(d8)>0:
            df1 = df1.assign(distancias_i8=d1)

        if sum(s1to)>0:
            df1=df1.assign(S1_TOX=s1to)
        if sum(s1ex)>0:
            df1=df1.assign(S1_EXP=s1ex)
        if sum(s1in)>0:
            df1=df1.assign(S1_INF=s1in)
        if sum(s2to)>0:
            df1=df1.assign(S2_TOX=s2to)
        if sum(s2ex)>0:
            df1=df1.assign(S2_EXP=s2ex)
        if sum(s2in)>0:
            df1=df1.assign(S2_INF=s2in)
        if sum(s3to)>0:
            df1=df1.assign(S3_TOX=s3to)
        if sum(s3ex)>0:
            df1=df1.assign(S3_EXP=s3ex)
        if sum(s3in)>0:
            df1=df1.assign(S3_INF=s3in)
        if sum(s4to)>0:
            df1=df1.assign(S4_TOX=s4to)
        if sum(s4ex)>0:
            df1=df1.assign(S4_EXP=s4ex)
        if sum(s4in)>0:
            df1=df1.assign(S4_INF=s4in)
        if sum(s5to)>0:
            df1=df1.assign(S5_TOX=s5to)
        if sum(s5ex)>0:
            df1=df1.assign(S5_EXP=s5ex)
        if sum(s5in)>0:
            df1=df1.assign(S5_INF=s5in)
        if sum(s6to)>0:
            df1=df1.assign(S6_TOX=s6to)
        if sum(s6ex)>0:
            df1=df1.assign(S6_EXP=s6ex)
        if sum(s6in)>0:
            df1=df1.assign(S6_INF=s6in)
        if sum(s7to)>0:
            df1=df1.assign(S7_TOX=s7to)
        if sum(s7ex)>0:
            df1=df1.assign(S7_EXP=s7ex)
        if sum(s7in)>0:
            df1=df1.assign(S7_INF=s7in)
        if sum(s8to)>0:
            df1=df1.assign(S8_TOX=s8to)
        if sum(s8ex)>0:
            df1=df1.assign(S8_EXP=s8ex)
        if sum(s8in)>0:
            df1=df1.assign(S8_INF=s8in)
        # lista de cabeceras
        lista_cabeceras=[]
        # añadir los maximos
        for column in df1:
            print(column)
            lista_cabeceras.append(column)
        if "distancias_i1" in lista_cabeceras:
            filtered_df = df1.drop(["distancias_i1"], axis=1)
        if ("distancias_i1" and "distancias_i2") in lista_cabeceras:
            filtered_df = df1.drop(["distancias_i1","distancias_i2"], axis=1)
        if ("distancias_i1" and "distancias_i2" and "distancias_i3") in lista_cabeceras:
            filtered_df = df1.drop(["distancias_i1","distancias_i2","distancias_i3"], axis=1)
        if ("distancias_i1" and "distancias_i2" and "distancias_i3" and "distancias_i4") in lista_cabeceras:
            filtered_df = df1.drop(["distancias_i1","distancias_i2","distancias_i3","distancias_i4"], axis=1)
        if ("distancias_i1" and "distancias_i2" and "distancias_i3" and "distancias_i4" and "distancias_i5") in lista_cabeceras:
            filtered_df = df1.drop(["distancias_i1","distancias_i2","distancias_i3","distancias_i4","distancias_i5"], axis=1)
        if ("distancias_i1" and "distancias_i2" and "distancias_i3" and "distancias_i4"and"distancias_i5"and"distancias_i6") in lista_cabeceras:
            filtered_df = df1.drop(["distancias_i1","distancias_i2","distancias_i3","distancias_i4","distancias_i5","distancias_i6"], axis=1)
        #oara 7
        if ("distancias_i1" and "distancias_i2" and "distancias_i3" and "distancias_i4" and "distancias_i5" and "distancias_i6"and"distancias_i7")in lista_cabeceras:
            filtered_df = df1.drop(
                ["distancias_i1", "distancias_i2", "distancias_i3", "distancias_i4", "distancias_i5", "distancias_i6","distancias_i7"],
                axis=1)
        if (
                    "distancias_i1" and "distancias_i2" and "distancias_i3" and "distancias_i4" and "distancias_i5" and "distancias_i6" and "distancias_i7"and "distancias_i8") in lista_cabeceras:
            filtered_df = df1.drop(
                    ["distancias_i1", "distancias_i2", "distancias_i3", "distancias_i4", "distancias_i5",
                     "distancias_i6", "distancias_i7","distancias_i8"],
                    axis=1)

        VEs = list(filtered_df.idxmax(axis=1))
        df1 = df1.assign(SELECT=VEs)
         #mostrar dataframe
        root = tk.Tk()
        table = table = DataFrameTable(root, df1)
        root.mainloop()



    def Guardar(self):
        global number
        global numero_ubicaciones
        number+=1
        
        atipo_sustancia = []
        atipo_sus_t_i_e = []
        acantidad_sustancia = []
        adistancias_s = []
        tipo_instalaciones.append(self.combo.currentText()) # tipo
        condiciones.append(self.comboBox_2.currentText())  # condiciones
        o1_=fun.buscar_o1(self.combo.currentText())
        o1.append(o1_)
        o2_=fun.buscar_o2(self.comboBox_2.currentText())
        o2.append(o2_)
        s1=(self.s1.currentText())#sustancia i
        c1=int(self.c1.value())
        s2 = (self.s2.currentText())  # sustancia i
        c2 = int(self.c2.value())
        s3 = (self.s3.currentText())  # sustancia i
        c3 = int(self.c3.value())
        s4 = (self.s4.currentText())  # sustancia i
        c4 = int(self.c4.value())
        s5 = (self.s5.currentText())  # sustancia i
        c5 = int(self.c5.value())
        s6 = (self.s6.currentText())  # sustancia i
        c6 = int(self.c6.value())
        s7 = (self.s7.currentText())  # sustancia i
        c7 = int(self.c7.value())
        s8 = (self.s8.toPlainText())  # sustancia i
        c8 = int(self.c8.value())
        if c1>0:
            atipo_sustancia.append(s1)
            acantidad_sustancia.append(c1)
        if c2>0:
            atipo_sustancia.append(s2)
            acantidad_sustancia.append(c2)
        if c3>0:
            atipo_sustancia.append(s3)
            acantidad_sustancia.append(c3)
        if c4>0:
            atipo_sustancia.append(s4)
            acantidad_sustancia.append(c4)
        if c5>0:
            atipo_sustancia.append(s5)
            acantidad_sustancia.append(c5)
        if c6>0:
            atipo_sustancia.append(s6)
            acantidad_sustancia.append(c6)
        if c7>0:
            atipo_sustancia.append(s7)
            acantidad_sustancia.append(c7)
        if c8>0:
            atipo_sustancia.append(s8)
            acantidad_sustancia.append(c8)

        tipo_sustancia.append(atipo_sustancia)
        cantidad_sustancia.append(acantidad_sustancia)
        o3_tox=0
        o3_inf=0
        o3_exp=0
        a_t = 0
        a_i = 0
        a_e = 0

        for i in range(len(acantidad_sustancia)):
            dis_a.append(i)
            a=atipo_sustancia[i]
            b=acantidad_sustancia[i]
            G,o3_,d,tipo=fun.buscar_G_y_o3_y_d(a,b)
            print(tipo)
            A=fun.Calcular_A(o1_,o2_,o3_,G,d)
            if tipo=='Toxica':
                o3_tox+=o3_
                a_t+=A
            elif tipo=='Inflamable':
                o3_inf+=o3_
                a_i+=A
            elif tipo=='Explosiva':
                o3_exp+=o3_
                a_e+=A
            else:
                pass
        o3_t.append(o3_tox)
        o3_i.append(o3_inf)
        o3_e.append(o3_exp)
        A_tox.append(a_t)
        A_inf.append(a_i)
        A_exp.append(a_e)
        #calculo para atox
        print("A toxico", a_t)
        print( "A explosivo", a_e)
        print( "A inflamable ", a_i)
        #las distancias
        d1 = int(self.d1.value())
        d2 = int(self.d2.value())
        d3 = int(self.d3.value())
        d4 = int(self.d4.value())
        d5 = int(self.d5.value())
        d6 = int(self.d6.value())
        d7 = int(self.d7.value())
        d8 = int(self.d8.value())
        contador.append(0)

        if d1 > 0:
            distancias_s.append(d1)
            j=fun.buscar_s(d1,a_t,'Toxica')
            k=fun.buscar_s(d1, a_i, 'Inflamable')
            l=fun.buscar_s(d1, a_e, 'Explosiva')
            s1t.append(j)
            s2e.append(l)
            s3i.append(k)
            contador.append(mm)
            numero_ubicaciones+=1




        if d2 > 0:
            distancias_s.append(d2)
            j = fun.buscar_s(d2, a_t, 'Toxica')
            k = fun.buscar_s(d2, a_i, 'Inflamable')
            l = fun.buscar_s(d2, a_e, 'Explosiva')

            s1t.append(j)
            s2e.append(l)
            s3i.append(k)
            contador.append(mm)
            numero_ubicaciones += 1


        if d3 > 0:
            distancias_s.append(d3)
            j = fun.buscar_s(d3, a_t, 'Toxica')
            k = fun.buscar_s(d3, a_i, 'Inflamable')
            l = fun.buscar_s(d3, a_e, 'Explosiva')

            s1t.append(j)
            s2e.append(l)
            s3i.append(k)
            contador.append(mm)
            numero_ubicaciones += 1

        if d4 > 0:
            distancias_s.append(d4)
            j = fun.buscar_s(d4, a_t, 'Toxica')
            k = fun.buscar_s(d4, a_i, 'Inflamable')
            l = fun.buscar_s(d4, a_e, 'Explosiva')

            s1t.append(j)
            s2e.append(l)
            s3i.append(k)
            contador.append(mm)
            numero_ubicaciones += 1
        if d5 > 0:
            distancias_s.append(d5)
            j = fun.buscar_s(d5, a_t, 'Toxica')
            k = fun.buscar_s(d5, a_i, 'Inflamable')
            l = fun.buscar_s(d5, a_e, 'Explosiva')

            s1t.append(j)
            s2e.append(l)
            s3i.append(k)
            contador.append(mm)
            numero_ubicaciones += 1

        if d6 > 0:
            distancias_s.append(d6)
            j = fun.buscar_s(d6, a_t, 'Toxica')
            k = fun.buscar_s(d6, a_i, 'Inflamable')
            l = fun.buscar_s(d6, a_e, 'Explosiva')

            s1t.append(j)
            s2e.append(l)
            s3i.append(k)
            contador.append(mm)
            numero_ubicaciones += 1


        if d7 > 0:
            distancias_s.append(d7)
            j = fun.buscar_s(d7, a_t, 'Toxica')
            k = fun.buscar_s(d7, a_i, 'Inflamable')
            l = fun.buscar_s(d7, a_e, 'Explosiva')

            s1t.append(j)
            s2e.append(l)
            s3i.append(k)
            contador.append(mm)
            numero_ubicaciones += 1


        if d8 > 0:
            distancias_s.append(d8)
            j = fun.buscar_s(d8, a_t, 'Toxica')
            k = fun.buscar_s(d8, a_i, 'Inflamable')
            l = fun.buscar_s(d8, a_e, 'Explosiva')

            s1t.append(j)
            s2e.append(l)
            s3i.append(k)
            contador.append(mm)
            numero_ubicaciones += 1
        else:
            pass


    def Salir(self):
        self.parent().show()
        self.close()

class Ventanaayuda(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanaayuda, self).__init__(parent)
        loadUi('prix3.ui', self)
        self.pushButton_r.clicked.connect(self.regresar)

    def regresar(self):
        self.parent().show()
        self.close()
        self.hide()
        otraventana = Cargar_datos(self)
        otraventana.show()
#aca pongo los de ayuda que son dos ventanas
class Ventanaayuda1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanaayuda1, self).__init__(parent)
        loadUi('prix5.ui', self)
        self.pushButton.clicked.connect(self.regresar)


    def regresar(self):
        self.hide()
        otraventana = Anadir(self)
        otraventana.show()
# sustancia añadida con exito
## ventanas ayuda
class Ventanaayuda2(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanaayuda2, self).__init__(parent)
        loadUi('prix6.ui', self)
        self.pushButton.clicked.connect(self.regresar)


    def regresar(self):
        self.hide()
        otraventana = Anadir(self)
        otraventana.show()
class Ventanaayuda3(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanaayuda3, self).__init__(parent)
        loadUi('prix7.ui', self)
        self.pushButton.clicked.connect(self.regresar)


    def regresar(self):
        self.hide()
        otraventana = Anadir(self)
        otraventana.show()

class Anadir(QMainWindow):
    def __init__(self, parent=None):
        super(Anadir, self).__init__(parent)
        loadUi('prix4.ui', self)
        self.boton5.clicked.connect(self.mostrar_msm)
        self.boton5.clicked.connect(self.guardar_sus)
        self.boton6.clicked.connect(self.salir)
        self.pushButton.clicked.connect(self.mostrar_msm1)
        self.pushButton_2.clicked.connect(self.mostrar_msm2)

    def salir(self):
        self.parent().show()
        self.close()
        self.hide()
        otraventana = Cargar_datos(self)
        otraventana.show()
    def mostrar_msm(self):
        self.hide()
        otraventana = Ventanaayuda1(self)
        otraventana.show()
    def mostrar_msm1(self):
        self.hide()
        otraventana = Ventanaayuda2(self)
        otraventana.show()
    def mostrar_msm2(self):
        self.hide()
        otraventana = Ventanaayuda3(self)
        otraventana.show()


        

    def guardar_sus(self):
        tipo=self.input4.currentText()
        if tipo=='Toxica':
            listas.sustancia_toxica.append(self.input1.toPlainText())
            listas.valor_limite_sustancia_toxica.append(self.input2.value())
            listas.factor_o3_sustancia_toxica.append(self.input2.value())

        if tipo=='Explosiva':
            listas.sustancia_Explosiva.append(self.input1.toPlainText())
            listas.valor_limite_sustancia_Explosiva.append(self.input2.value())
            listas.factor_o3_sustancia_Explosiva.append(self.input2.value())

        if tipo=='Inflamable':
            listas.sustancia_Inflamable.append(self.input1.toPlainText())
            listas.valor_limite_sustancia_Inflamable.append(self.input2.value())
            listas.factor_o3_sustancia_Inflamable.append(self.input2.value())
        else:
            pass
        


app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())