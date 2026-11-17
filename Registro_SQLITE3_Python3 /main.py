import sqlite3
from pathlib import Path
from datetime import datetime
import math

def crear_tabla(archivo):
    conexion = sqlite3.connect(f'{archivo}', isolation_level=None)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_vehiculo TEXT NOT NULL,
            placas TEXT NOT NULL,
            color TEXT NOT NULL,
            hora_entrada TEXT NOT NULL,
            hora_salida TEXT,
            monto_pagado REAL
        )
    """)

    cursor.close()
    menu(conexion)

def menu(conexion):
    while True:
        print('~~~~~~~BIENVENIDO AL MENU~~~~~~~')
        print('1-Registrar Entrada.')
        print('2-Ver Vehiculos Estacionados.')
        print('3-Registrar Salida y Cobrar.')
        print('4-Borrar Vehiculo.')
        print('5-Salir.')
        opcion = int(input('>'))
        if opcion == 1:
            registrar_entrada(conexion)
        elif opcion == 2:
            ver_vehiculos(conexion)
        elif opcion == 3:
            salida_cobrar(conexion)
        elif opcion == 4:
            borrar_vehiculo(conexion)
        elif opcion == 5:
            conexion.close()
            break

def ver_vehiculos(conexion):
    cursor = conexion.cursor()
    while True:
        print('##===BUSCAR EN EL REGISTRO===##')
        print('1-Ver tabla completa.')
        print('2-Buscar en la tabla.')
        print('3-Salir')
        desicion = int(input('>'))
        if desicion == 2:
            print('1-Por nombre.')
            print('2-Por matricula.')
            desicion2 = int(input('>'))
            if desicion2 == 1:
                buscar = str(input('Ingrese el nombre del vehiculo (s para salir): ')).upper()
                if buscar != 'S':
                    cursor.execute('SELECT * FROM registros WHERE tipo_vehiculo LIKE ?', (f"%{buscar}%",))
                    encontrar = cursor.fetchall()
                    if encontrar:
                        print('--------VEHICULO ENCONTRADO--------')
                        print(encontrar)
                        print('-----------------------------------')
                    else:
                        print('Vehiculo no encontrado, desea agregarlo?')
                        opcion = str(input('(Si/No): ')).upper()
                        if opcion == 'SI':
                            registrar_entrada(conexion)
                            cursor.close()
                            break
                        elif opcion == 'NO':
                            cursor.close()
                            break
                        else:
                            print('Solo si o no.\n')
                else:
                    break

            elif desicion2 == 2:

                buscar2 = str(input('Ingrese el nombre del vehiculo (s para salir): ')).upper()
                if buscar2 != 'S':
                    cursor.execute('SELECT * FROM registros WHERE placas LIKE ?', (f"%{buscar2}%",))
                    encontrar2 = cursor.fetchall()
                    if encontrar2:
                        print('--------VEHICULO ENCONTRADO--------')
                        print(encontrar2)
                        print('-----------------------------------')
                    else:
                        print('Vehiculo no encontrado, desea agregarlo?')
                        opcion2 = str(input('(Si/No): ')).upper()
                        if opcion2 == 'SI':
                            registrar_entrada(conexion)
                            cursor.close()
                            break
                        elif opcion2 == 'NO':
                            cursor.close()
                            break
                        else:
                            print('Solo si o no.\n')
                else:
                    break

        elif desicion == 1:
            cursor.execute('SELECT * FROM registros ORDER BY tipo_vehiculo')
            tabla = cursor.fetchall()
            print('\n-----------------------------------TABLA----------------------------------')
            for fila in tabla:
                print(fila)

            print('--------------------------------------------------------------------------')
            salir = str(input('s para salir')).upper()
            if salir == 'S':
                cursor.close()
                break
            else:
                print('Solo "s".')
        elif desicion == 3:
            cursor.close()
            break
        else:
            print('Ingrese un numero valido.\n')



def registrar_entrada(conexion):
    cursor = conexion.cursor()
    while True:
        opcion = str(input('Ingresar datos ala tabla?: (Si/No)')).upper()
        if opcion == 'SI':
            vehiculo = str(input('Nombre del vehiculo: '))
            placas = input('Placas: ')
            color = str(input('Color: '))
            hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(f'INSERT INTO registros (tipo_vehiculo, placas, color, hora_entrada) VALUES (?, ?, ?, ?)', [vehiculo, placas, color, hora])
            print('Agregado con exito!!.\n')
            print(f'Vehiculo: {vehiculo}, Hora: {hora}')
            continue
        elif opcion == 'NO':
            cursor.close()
            break
        else:
            print('Solo si o no.\n')


def salida_cobrar(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id, tipo_vehiculo, placas, hora_entrada
        FROM registros
        WHERE hora_salida IS NULL
       """)

    autos_activos = cursor.fetchall()

    if not autos_activos:
        print('No hay autos estacionados.\n')
        cursor.close()
        return

    print('\n------AUTOS ACTUALMENTE ESTACIONADOS------\n')
    for indice, auto in enumerate(autos_activos, start=1):
        id_reg, vehiculo, placa, entrada = auto
        print(f"{indice}. Vehiculo: {vehiculo}, Placa: {placa} | Entrada: {entrada}")

    try:
        opcion = int(input('Seleccione el numero del vehiculo que saldra: '))
        if opcion < 1 or opcion > len(autos_activos):
            print('Opcion no valida.\n')
            cursor.close()
            return
    except ValueError:
        print('Por favor ingresa un numero valido.\n')
        cursor.close()
        return

    id_registro, vehiculo, placa, entrada_str = autos_activos[opcion - 1]


    hora_entrada = datetime.strptime(entrada_str, "%Y-%m-%d %H:%M:%S")
    hora_salida = datetime.now()

    diferencia = hora_salida - hora_entrada
    horas_transcurridas = diferencia.total_seconds() / 3600
    horas_a_cobrar = max(1, math.ceil(horas_transcurridas))
    pesos_hora = 15
    monto_pagado = horas_a_cobrar * pesos_hora

    salida_str = hora_salida.strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        UPDATE registros
        SET hora_salida = ?, monto_pagado = ?
        WHERE id = ?
        """,
            (salida_str, monto_pagado, id_registro),
    )

    print('Listo!!.\n')
    print(f'Total: {monto_pagado}, Vehiculo: {vehiculo}, Placas: {placa}')
    cursor.close()
    return

def borrar_vehiculo(conexion):
    cursor = conexion.cursor()

    while True:
        print('#----DESEA ELIMINAR UN VEHICULO DEL REGISTRO----#')
        print('1-Eliminar')
        print('2-Salir')
        opcion = int(input('>'))
        
        if opcion == 1:
            cursor.execute('SELECT * FROM registros ORDER BY tipo_vehiculo')
            tabla = cursor.fetchall()
            print('\n-----------------------------------TABLA----------------------------------')
            for fila in tabla:
                print(fila)

            print('--------------------------------------------------------------------------')
            
            borrar = input('Seleccione el numero del vehiculo a borrar: ')
            cursor.execute('DELETE FROM registros WHERE id = (?)', [borrar])
            
            if cursor.rowcount > 0:
                print('Borrado con exito!!.\n')
                continue
            else:
                print('No se encontro el vehiculo, deseas salir? (Si/No)')
                respuesta = input('>').upper()
                if respuesta == 'SI':
                    cursor.close()
                    break
                elif respuesta == 'NO':
                    continue
                else:
                    print('Solo si o no.\n')
        elif opcion == 2:
            cursor.close()
            break

##############################################################################################################################################
##############################################################################################################################################

print('#=====BIENVENIDO=====#')

nameArch = input('Ingresa el nombre del archivo: ')
archivo = Path(f"{nameArch}.db")

if archivo.exists():
    print('Se abrio un archivo existente!!.\n')
    conexion = sqlite3.connect(f'{archivo}', isolation_level=None)
    menu(conexion)
else:
    print('Archivo Creado!!.\n')
    crear_tabla(archivo)

