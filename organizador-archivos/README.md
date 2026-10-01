#=====ORGANIZADOR DE DOCUMENTOS, ARCHIVOS ETC=====#

#===FUNCIONES===#
def copiar_archivos(): 
    import shutil as s
    from pathlib import Path as p

    h = p.home()
    try:
        origen = input("Ingrese la ruta de origen: ")
        destino = input("Ingrese la ruta de destino: ")

        s.copy(h / f'{origen}', h / f'{destino}')

        print(f"Archivos copiados de {origen} a {destino} exitosamente.")
    except Exception as e:
        print(f"\n\tNo se pudo copiar los archivos, Razon del fallo: {e}\n")
        return
#===USAMOS LOS MODULOS SHUTIL Y PATH PARA COPIAR ARCHIVOS MEDIANTE RUTAS, UBICANDO AL USUARIO MEDIANTE HOME, USAMOA TRY Y EXCEPT PARA CAPTURAR ERRORES===#
    
def mover_archivos():
    import shutil as s
    from pathlib import Path as p

    h = p.home()
    try:
        origen = input("Ingrese la ruta de origen: ")
        destino = input("Ingrese la ruta de destino: ")

        s.move(h / f'{origen}', h / f'{destino}')

        print(f"\n\tArchivos movidos de {origen} a {destino} exitosamente.\t\n")
    except Exception as e:
        print(f"\n\tNo se pudo mover los archivos, Razon del fallo: {e}\n")
        return

#===DEL MISMO MODO IMPORTAMOS LOS MISMOS MODULOS Y EL MISMO BLOQUE CODIGO CON LA DIFERENCIA DE QUE USAMOS MOVE PARA MOVER ARCHIVOS A OTRAS CARPETAS===#

def copiar_carpeta():
    import shutil as s
    from pathlib import Path as p

    h = p.home()
    try:
        origen = input("Ingrese la ruta de origen: ")
        destino = input("Ingrese la ruta de destino: ")

        s.copytree(h / f'{origen}', h / f'{destino}')

        print(f"\n\tCarpeta copiada de {origen} a {destino} exitosamente.\t\n")
    except Exception as e:
        print(f"\n\tNo se pudo copiar la carpeta, Razon del fallo: {e}\n")
        return

#===DEL MISMO MODO IMPORTAMOS LOS MISMOS MODULOS Y EL MISMO BLOQUE CODIGO CON LA DIFERENCIA DE QUE USAMOS COPYTREE PARA COPIAR CARPETAS A OTRAS CARPETAS===#

def mover_carpeta():
    mover_archivos()

#==ES LO MISMO QUE MOVER ARCHIVOS YA QUE ES EL MISMO BLOQUE DE CODIGO, QUIZA DEBERIA DE ESCXRIBIRLO PARA QUE QUEDE BIEN, JAJAJ==# 


def eliminar_carpeta():
    import shutil as s
    from pathlib import Path as p

    h = p.home()
    try:
        carpeta = input("Ingrese la ruta de la carpeta a eliminar: ")

        s.rmtree(h / f'{carpeta}')

        print(f"\n\tCarpeta {carpeta} eliminada exitosamente.\t\n")
    except Exception as e:
        print(f"\n\tNo se pudo eliminar la carpeta, Razon del fallo: {e}\n")
        return

#===DE IGUAL FORMA SE USA LA MISMA ESTRUCURA DE CODIGO, PERO USANDO RMTREE PARA ELIMINAR CARPETAS, RECORDEMOS QUE ES MEDIANTE RUTAS, ASI QUE SERA IGUAL.===#

def eliminar_archivos():
    import os as o
    from pathlib import Path as p

    h = p.home()
    try:
        archivos = input('Ingrese la ruta de los archivos a eliminar: ')

        o.remove(h / f'{archivos}')
        print(f"\n\tArchivos {archivos} eliminados exitosamente.\t\n")
    except Exception as e:
        print(f"\n\tNo se pudo eliminar los archivos, Razon del fallo: {e}\n")
        return

#===ESTA VEZ IMPORTO EL MODULO OS, QUE ME AYUDARA A REMOVER LOS ARCHIVOS, DE ACUERDO ALA RUTA QUE TRAZE EL USUARIO, USANDO REMOVE PARA ELIMINAR LOS ARCHIVOS===#

def ver_archivos():
    import os as o
    from pathlib import Path as p

    h = p.home()
    try:
        ruta = input("Ingrese la ruta de la carpeta: ")
        archivos = o.listdir(h / f'{ruta}')
        print(f"\n\tArchivos en la carpeta {ruta}:\t\n")
        for archivo in archivos:
            print(f'archivo\n')
    except Exception as e:
        print(f"\n\tNo se pudo listar los archivos, Razon del fallo: {e}\n")
        return

#===USO LA FUNCION LISTDIR PARA QUE ME LISTE TODOS LOS ARCHIVOS DE UNA CARPETA, USO UN CICLO FOR PARA IMPRIMI TODOS LOS ARCHIVOS, DE IGUAL FORMA USO EL TRY Y EXCEPT PARA CAPTURAR ERRORES===# 


#===MENU PRINCIPAL===#
while True:
    print("Bienvenido al organizador de documentos")
    print("1. Organizar\n")
    print("2. Salir\n")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        while True:
            print("1-Copiar archivos\n")
            print("2-Mover archivos\n")
            print("3-Copiar carpeta\n")
            print("4-Mover carpeta\n")
            print("5-Eliminar carpeta\n")
            print("6-Eliminar archivos\n")
            print("7-Ver archivos de una carpeta\n")
            print("8-Crear ZIP de una carpeta\n")
            print("9-Extraer archivos de un ZIP\n")
            print("10-Volver al menú principal\n")
            opcion2 = int(input("Seleccione una opción: "))

            if opcion2 == 1:
                copiar_archivos()
            elif opcion2 == 2:
                mover_archivos()
            elif opcion2 == 3:
                copiar_carpeta()
            elif opcion2 == 4:
                mover_carpeta()
            elif opcion2 == 5:
                eliminar_carpeta()
            elif opcion2 == 6:
                eliminar_archivos()
            elif opcion2 == 7:
                ver_archivos()
            elif opcion2 == 8:
                print("Función de crear ZIP aún no implementada.")
            elif opcion2 == 9:
                print("Función de extraer ZIP aún no implementada.")
            elif opcion2 == 10:
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.\n")
            
    elif opcion == 2:
        import time as t #Algo de estilo.
        print("Saliendo del organizador de documentos..."); t.sleep(3)
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.\n")
