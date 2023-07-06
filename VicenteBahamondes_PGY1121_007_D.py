def ver_menu():
    print("""MENÚ
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")

def validar_opcion():
    while True:
        try:            
            opc = int(input("Elija una opcion: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR! OPCION INVALIDA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO")

def validar_compra():
    while True:
        try:
            compra = int(input("Elija la cantidad de entradas que desea comprar (1-3): "))
            if compra >= 1 and compra <=3:
                return compra
            else:
                print("EL MAXIMO DE ENTRADAS A COMPRAR ES DE 3")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO")

def validar_rut():
    while True:        
        try:    
            rut = int(input("Ingrese su RUT (Sin guion, puntos ni dígito verificador): "))
            if len(str(rut)) >7 and len(str(rut)) <=8:
                return rut
            elif rut in lista_ruts:
                print("ESTE RUT YA ESTA REGISTRADO")
            else:
                print("ERROR! EL RUT DEBE TENER 8 NÚMEROS")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO")

import numpy as np
concierto = np.zeros((10,10), int)
lista_ruts = []
lista_compra = []
lista_filas = []
lista_columnas = []
lista_entradas_p = []
lista_entradas_g = []
lista_entradas_s = []

def ver_escenario():
    for x in range (10):
        print(f"FILAS {x+1}", end= " ")
        for y in range(10):
            print(concierto[y][x], end="")

def validar_filas():
     while True:      
        try:   
            filas = int(input("Elija una fila (1-10): "))
            if filas >=1 and filas <=10:
                return filas
            else:
                print("DEBE INGRESAR UNA FILA ENTRE 1 Y 10")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO")   

def validar_columna():
    while True:
        try:
            columnas = int(input("Elija una columna (1-10): "))
            if columnas >=1 and columnas <=10:
                lista_entradas_g.append(columnas)
                lista_entradas_p.append(columnas)
                lista_entradas_s.append(columnas)
                return columnas
            else:
                print("ERROR! DEBE INGRESAR UN COLUMNA ENTRE 1 Y 10")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO")

def validar_compra_entradas():
    ("COMPRAR ENTRADAS")
    compra = validar_compra()
    escenario = ver_escenario()
    rut = validar_rut()
    fila = validar_filas()
    columna = validar_columna()
    while True:
        if concierto [fila-1][columna-1] == 0:
            concierto [fila-1][columna-1] = 1
            lista_compra.append(compra)
            lista_ruts.append(rut)
            lista_filas.append(fila)
            lista_columnas.append(columna)
            print("La opareación se a realizado correctamnete")
            return

def ver_ubicaciones():
    for x in range (10):
        print(f"FILAS {x+1}", end= " ")
        for y in range(10):
            print(concierto[x][y],end="")

def ver_asistentes():
    print (lista_ruts)

def ver_ganancias():
    ganacias_p = 150000 * 1 + lista_entradas_p
    ganacias_g = 80000  * 1 + lista_entradas_g
    ganacias_s = 50000  * 1 + lista_entradas_s
    cantidad = lista_entradas_s + lista_columnas + lista_entradas_p
    total = ganacias_g + ganacias_p + ganacias_s
    print("Platinum         ",lista_entradas_p,"        ",ganacias_p)
    print("Gold             ",lista_entradas_g,"        ",ganacias_g)
    print("Silver           ",lista_entradas_s,"        ",ganacias_s)
    print("TOTAL            ",cantidad,"        ",total)