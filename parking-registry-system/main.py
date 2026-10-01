#===MINI PROGRAMA PENSADO PARA UN ESTACIONAMIENTO===#
def menu():
	while True:
		print('\n\n\n\n\n\n\n\n\n\n\n\n#===·Bienvenido·===#')
		print('1-Añadir vehiculo\n')
		print('2-Buscar vehiculo\n')
		print('3-Borrar vehiculo\n')
		print('4-Finalizar\n')
		try:
			opcion = int(input('>\n\n'))
		except ValueError as v:
			print(f'\n{v} Ingresa un numero de los que indica.\n'); t.sleep(5)
			continue

		if opcion == 1:
			addVehicle(nombre_carpeta, nombre_archivo)
		elif opcion == 2:
			search_vehicle(nombre_carpeta, nombre_archivo)
		elif opcion == 3:
			delete_vehicle(nombre_carpeta, nombre_archivo)
		elif opcion == 4:
			return

def delete_vehicle(nombre_carpeta, nombre_archivo):
	from pathlib import Path as p
	h = p.home()
	while True:
		borrar_vehiculo = str(input('Ingrese el modelo del vehiculo a borrar: '))
		with open(h / f'{nombre_carpeta}/{nombre_archivo}', 'r') as f:
			lineas = f.readlines()
		with open(h / f'{nombre_carpeta}/{nombre_archivo}', 'w') as f:
			for linea in lineas:
				if borrar_vehiculo not in linea.strip():
					f.write(linea)
		print(f'\nVehiculo {borrar_vehiculo} borrado de la lista.\n')
		try:
			respuesta = str(input('\nDesea borrar otro vehiculo? (s/n): ')).lower()
		except ValueError as v:
			print(f'\n{v} Ingresa s o n.\n'); t.sleep(5)
			continue
		if respuesta == "s":
			continue
		elif respuesta == "n":
			break
def crear_carpeta():
	global nombre_carpeta
	while True:	
		from pathlib import Path as p
		h = p.home()
		try:
			nombre_carpeta = str(input('\n>(Nombre de la carpeta):  '))
		except ValueError as v:
			print(f'\n{v} El archivo no puede empezar por un numero.\n'); t.sleep(5)
			continue

		try:
			(h / f'{nombre_carpeta}').mkdir(exist_ok=True)
			print(f'\n\nLA CARPETA {nombre_carpeta} AH SIDO CREADA!!\n\n')
		except OSError as e:
			print(f'\nNo se pudo crear la carpeta: {e}\n')
			continue


		try:
			respuesta = str(input('\nDesea crear un archivo dentro de la carpeta? (s/n): ')).lower()
		except ValueError as v:
			print(f'\n{v} Ingresa s o n.\n'); t.sleep(5)
			
		if respuesta == "s":
			crear_archivo()
			break
		elif respuesta == "n":
			break
		else:
			print('\nIngresa s o n.\n'); t.sleep(3)

def crear_archivo():
	global nombre_archivo

	from pathlib import Path as p
	h = p.home()

	while True:
		
		nombre_archivo = input('\nIngresa el nombre del archivo Ejemplo: (nombre.txt): ')

		try:
			with open(h / f'{nombre_carpeta}/{nombre_archivo}', 'w', encoding='utf-8'):
				print(f'\nLISTO!! La carpeta: {nombre_carpeta} y el archivo: {nombre_archivo} HAN SIDO CREADOS!!\n')
				break
		except OSError as e:
			print(f'\nNo se pudo crear el archivo: {e}\n')
			continue

		try:
			respuesta = str(input('\nDesea ingresar al menu de opciones? (s/n): ')).lower()

		except ValueError as v:
			print('\nIngresa lo que pide.\n'); t.sleep(5)
			continue


		if respuesta == "s":
			menu()
			break
		elif respuesta == "n":
			break
		else:
			print('\nIngresa s o n.\n'); t.sleep(3)

def search_vehicle(nombre_carpeta, nombre_archivo):
	import re as r
	from pathlib import Path as p
	h = p.home()
	encontrado = False
	modelo_del_vehiculo = str(input('Ingrese el modelo del vehiculo a buscar: '))
	with open(h / f'{nombre_carpeta}/{nombre_archivo}', 'r') as f:
		for linea in f:
			if r.search(modelo_del_vehiculo, linea, r.IGNORECASE):
				print(f'\nVehiculo encontrado: {linea.strip()}\n')
				encontrado = True

	if not encontrado:
		print(f'\nVehiculo no encontrado.\n')
		print('Desea agregar el vehiculo a la lista? (s/n): ')
		respuesta = input('>')
		if respuesta.lower() == 's':
			addVehicle(nombre_carpeta, nombre_archivo)
		elif respuesta.lower() == 'n':
			print('\nNo se agregara el vehiculo a la lista.\n')
			menu()

def addVehicle(nombre_carpeta, nombre_archivo):
	from pathlib import Path as p
	h = p.home()
	while True:
		print('Ingrese el vehiculo, seguido de las placas, seguido del color, seguido de la hora de entrada (en un mismo renglon): (s para salir)')
		agregar_vehiculo = input('>')
		with open(h / f'{nombre_carpeta}/{nombre_archivo}', 'a', encoding='utf-8') as arch:
			if agregar_vehiculo.lower() == 's':
				break
			arch.write(f'{agregar_vehiculo}\n')
			print('\nListo el vehiculo a sido agregado!\n')



while True:
	import time as t
	print('\n\n\n\n\n··Bienvenido··\n')
	print('Desea crear un nuevo registro para el dia de hoy?\n\n')
	try:
		opcion = str(input('\nSi/No-(usar uno ya existente), s para salir: \n\n')).lower()
	except ValueError as v:
		print(f'\n{v} Solo ingresa si o no.\n'); t.sleep(5)
		continue
	if opcion == "si":
		crear_carpeta()
		




	elif opcion == "no":
		from pathlib import Path as p
		h = p.home()
		existe = False

		nombre_carpeta = str(input('\n>(Recuerdeme el nombre de la carpeta):  '))
		if (h / f'{nombre_carpeta}').exists():
			print(f'\nLISTO!! La carpeta: {nombre_carpeta} EXISTE!!\n')
			
			nombre_archivo = str(input('\nTambien el nombre del archivo Ejemplo: (nombre.txt): '))
			if (h / f'{nombre_carpeta}/{nombre_archivo}').exists():
				print(f'\nLISTO!! La carpeta: {nombre_carpeta} y el archivo: {nombre_archivo} EXISTEN!!\n')
				existe = True
				menu()
			else:
				print(f'\nLa carpeta: {nombre_carpeta} EXISTE, pero el archivo: {nombre_archivo} NO EXISTE!!\n')
				existe = False
				print('\nDesea crear el archivo? (s/n): ')
				respuesta = input('>')
				if respuesta.lower() == 's':
					crear_archivo()
				elif respuesta.lower() == 'n':
					print('\nNo se creara el archivo.\n')
					continue
		else:
			print(f'\nLa carpeta: {nombre_carpeta} NO EXISTE!!\n')
			existe = False
			print('\nDesea crear la carpeta y el archivo? (s/n): ')
			respuesta = input('>')
			if respuesta.lower() == 's':
				crear_carpeta()
			elif respuesta.lower() == 'n':
				print('\nNo se creara la carpeta ni el archivo.\n')
				continue


	elif opcion == "s":
		break
	else:
		print('\nIngrese lo que pide.\n'); t.sleep(3)
		continue
