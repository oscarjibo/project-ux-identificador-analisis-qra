import listas


def buscar_o1(tipo_instalacion):
    if tipo_instalacion=="Almacenamiento":
        o1=0.1
    if tipo_instalacion=="Proceso":
        o1=1.0
    return float(o1)


def buscar_G_y_o3_y_d (tipo_sustancia,cantidad):
    d2=float(cantidad)
    G2=float()
    o32=float()
    tipo2=str()
    for i in range(len(listas.sustancia_toxica)):
        if tipo_sustancia==listas.sustancia_toxica[i]:
                G2=listas.valor_limite_sustancia_toxica[i]
                o32=listas.factor_o3_sustancia_toxica[i]
                tipo2="Toxica"
        else:
            pass

    for i in range(len(listas.sustancia_Inflamable)):
        if tipo_sustancia==listas.sustancia_Inflamable[i]:
                G2=listas.valor_limite_sustancia_Inflamable[i]
                o32=listas.factor_o3_sustancia_Inflamable[i]
                tipo2="Inflamable"
        else:
            pass

    for i in range(len(listas.sustancia_Explosiva)):
        if tipo_sustancia==listas.sustancia_Explosiva[i]:
                G2=listas.valor_limite_sustancia_Explosiva[i]
                o32=listas.factor_o3_sustancia_Explosiva[i]
                tipo2="Explosiva"
        else:
            pass

    print(G2,o32)
    return(G2,o32,d2,tipo2)

def buscar_o2(condicion):
    if (condicion=="Abierto" or condicion=="Condicion B"):
        o2=1.0
    if (condicion == "Cerrado" or condicion=="Condicion A"):
        o2 = 0.1
    return float(o2)

def buscar_s(distancia,a,tipo):
    S=0
    if tipo=="Toxica":
        S=(((100/distancia)**2)*a)
        print("S toxico:",S,"distancia :",distancia)
    else:
        pass
    if tipo=="Inflamable":
        S = (((100 / distancia) ** 3) * a)
        print("S inflamable", S, "distancia :", distancia)

    else:
        pass

    if tipo=="Explosiva":
        S = (((100 / distancia) ** 3) * a)
        print("S Explosiva", S, "distancia :", distancia)
    else:
        pass

    return (S)

def Calcular_A(o1,o2,o3,g,q):
    A=(o1*o2*o3*q)/g
    return A


