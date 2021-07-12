# arrancamo

import listas.py
import fun


# numero de instalacion

numero_instalaciones=int(input())
instalacion=[]
tipo_instalaciones=[]
numero_sustancias=[]
tipo_sustancia=[]
tipo_sus_t_i_e=[]
cantidad_sustancia=[]
condiciones=[]
o1=[]
o2=[]
o3=[]
g=[]
d=[]
A_sus=[]
num_dis=[]
distancias_s=[]
for i in range(1,numero_instalaciones+1):
    print("tipo de instalacion (Almacenamiento) (Proceso)", i,":")
    tipo_in = (input())
    print("ingrese condiciones de instalacion 'Aire libre' 'Cerrada' 'condicion A' 'condicion B': ") # - instalación al aire libre: 1.0
    condicion=(input())
    print("ingrese cuantas sustancias hay en instacion :",i)
    sustancias = []
    cantidades = []
    distancias = []
    numero_sustancia=int(input())
    for h in range(1,numero_sustancia+1):
        print("ingrese sustancia :",h, " de instalacion :",i)
        sus=input()
        sustancias.append(sus)
        print("ingrese cantidad de sustancia :", h, " de instalacion :", i)
        cant=input()
        cantidades.append(cant)



    tipo_sustancia.append(sustancias)
    cantidad_sustancia.append(cantidades)
    instalacion.append(i)
    tipo_instalaciones.append(tipo_in)
    condiciones.append(condicion)
    numero_sustancias.append(numero_sustancia)
    distancias_s.append(distancias)


for i in range(len(instalacion)):
    print("===================================")
    print("INSTALACION ",i+1)
    print("===================================")
    g_sus = []
    o3_sus = []
    d_sus = []
    tipo_sus=[]
    a_sus=[]
    # iniciamos los factores A
    A_tox=0
    A_inf=0
    A_exp=0
    # para las distancias
    # inicio cilos
    print( "| instalacion :", instalacion[i] , " | tipo :" , tipo_instalaciones [i], "| sustancia: ", tipo_sustancia[i],"| cantidad : ", cantidad_sustancia[i],"| condicion :", condiciones[i])
    o_1=fun.buscar_o1(tipo_instalaciones[i])
    o1.append(o_1)
    print("| o1","instalacion:",instalacion[i]," = ",o_1)
    o_2=fun.buscar_o2(condiciones[i])
    o2.append(o_2)
    print("| o2","instalacion:",instalacion[i]," = ",o_2)
    for t in range(numero_sustancias[i]):
        g1,o31,d1,Tipo1= fun.buscar_G_y_o3_y_d(tipo_sustancia[i][t],cantidad_sustancia[i][t])
        A=fun.Calcular_A(o_1,o_2,o31,g1,d1)
        g_sus.append(g1)
        o3_sus.append(o31)
        d_sus.append(d1)
        tipo_sus.append(Tipo1)
        a_sus.append(A)
        print("para instalacion:",i+1,"sustancia:",Tipo1," el factor A es:",A)
        if Tipo1=="Toxica":
            A_tox +=A
        else:
            pass
        if Tipo1=="Inflamable":
            A_inf +=A
        else:
            pass
        if Tipo1=="Explosiva":
            A_exp +=A
        else:
            pass
    print("num_ind tox = ", A_tox)
    print("num_ind inf = ", A_inf)
    print("num_ind exp = ", A_exp)


    o3.append(o3_sus)
    g.append(g_sus)
    d.append(d_sus)
    A_sus.append(a_sus)
    tipo_sus_t_i_e.append(tipo_sus)
    print("==============================")
    # agregamos las distancias
    print("ingrese cuantas distancias desea conocer")
    num_di = int(input())
    num_dis.append(num_di)
    for p in range(1, num_di + 1):
        print("ingrese distancia :", p, " para instalacion:",i+1)
        dis_n = float(input())
        fun.buscar_s(dis_n,A_tox,"Toxica")
        fun.buscar_s(dis_n,A_inf,"Inflamable")
        fun.buscar_s(dis_n,A_exp,"Explosiva")


