import VicenteBahamondes_PGY1121_007_D as fn

while True:
    fn.ver_menu()
    opc = fn.validar_opcion()
    if opc == 1:
        fn.validar_compra_entradas()
    elif opc == 2:
        fn.ver_ubicaciones()
    elif opc == 3:
        fn.ver_asistentes()
    elif opc == 4:
        fn.ver_ganancias()
    else:
        print("""ADIOS
    Nombre: Vicente
    Apellido: Bahamondes
    Fecha: 06-07-2023""")
        break
