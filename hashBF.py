import hashlib
import sys
import os

def selectOP(op):
	operSist = sys.platform
	if operSist == 'win32':
		if op == 1:
			return os.system('cls')
		elif op == 2:
			return os.system('chdir')
		elif op == 3:
			return os.system('pause>nul')
	elif operSist == 'linux':
		if op == 1:
			return os.system('clear')
		elif op == 2:
			return os.system('pwd')
		elif op == 3:
			return os.system('read -p ""')
	else:
		return '¡No se reconoce el sistema operativo!'
		exit()

def options(op):
	dec = input('\nA (Atras) | R (Repetir Operación) | S (Salir): ').lower()
	if dec == 'a':
		menu()
	elif dec == 'r':
		if op == 1:
			response = hashBF()
			if response == None:
				print('\nNo se ha podido romper la clave')
			else:
				print(response)
			options(1)
		elif op == 2:
			res = traduct()			
			print(res)
			if res[1] == 'S':
				selectOP(2)
			options(2)
		elif op == 3:
			print(hashingFile())
	elif dec == 's':
		selectOP(1)
		exit()
	else:
		print('¡Por favor, elija una opción correcta!')
		selectOP(3)
		options(op)

def hashBF():
	selectOP(1)
	resolverHash = input("\nHash a resolver: ")
	rutDoc = input('Añada el nombre del diccionario o su ruta absoluta: ')
	try:
		resolvedor = open(rutDoc, "r")

		print('\n1) SHA1')
		print('2) SHA224')
		print('3) SHA256')
		print('4) SHA384')
		print('5) SHA512')
		print('6) BLAKE2B')
		print('7) BLAKE2S')
		print('8) MD5')
		op = input('\nElija una opción: ')

		if op == '1':
			for x in resolvedor:
				a = hashlib.sha1(x.encode()).hexdigest()
				if a == resolverHash:
					return "\nClave: {} Este Hash fue resuelto: {}".format(x,a)
		elif op == '2':
			for x in resolvedor:
				a = hashlib.sha224(x.encode()).hexdigest()
				if a == resolverHash:
					return "\nClave: {} Este Hash fue resuelto: {}".format(x,a)
		elif op == '3':
			for x in resolvedor:
				a = hashlib.sha256(x.encode()).hexdigest()
				if a == resolverHash:
					return "\nClave: {} Este Hash fue resuelto: {}".format(x,a)
		elif op == '4':	
			for x in resolvedor:
				a = hashlib.sha384(x.encode()).hexdigest()
				if a == resolverHash:
					return "\nClave: {} Este Hash fue resuelto: {}".format(x,a)
		elif op == '5':
			for x in resolvedor:
				a = hashlib.sha512(x.encode()).hexdigest()
				if a == resolverHash:
					return "\nClave: {} Este Hash fue resuelto: {}".format(x,a)
		elif op == '6':	
			for x in resolvedor:
				a = hashlib.blake2b(x.encode()).hexdigest()
				if a == resolverHash:
					return "\nClave: {} Este Hash fue resuelto: {}".format(x,a)
		elif op == '7':
			for x in resolvedor:
				a = hashlib.blake2s(x.encode()).hexdigest()
				if a == resolverHash:
					return "\nClave: {} Este Hash fue resuelto: {}".format(x,a)
		elif op == '8':
			for x in resolvedor:
				a = hashlib.md5(x.encode()).hexdigest()
				if a == resolverHash:
					return "\nClave: {} Este Hash fue resuelto: {}".format(x,a)
		else:
			print('Por favor, elija una opción correcta')
			selectOP(3)
			return hashBF()

	except:
		return '\nNo se ha encontrado el archivo especificado'

def traduct():
	selectOP(1)
	txtDoc = input('Agregue el nombre del archivo en texto plano que desea traducir: ')
	txtTra = input('Elija el nombre del archivo traducido: ')

	try:
		fRead = open(txtDoc, "r")
		fWrite = open(txtTra, "a")

		print('\n1) SHA1')
		print('2) SHA224')
		print('3) SHA256')
		print('4) SHA384')
		print('5) SHA512')
		print('6) BLAKE2B')
		print('7) BLAKE2S')
		print('8) MD5')
		op = input('\nElija una opción: ')

		if op == '1':
			for line in fRead:
				fWrite.write(hashlib.sha1(line.encode()).hexdigest())
				fWrite.write("\n")
			fRead.close()
			fWrite.close()
			return '\nSe ha completado la traducción de hashes!\nArchivo guardado en: \n'
		elif op == '2':
			for line in fRead:
				fWrite.write(hashlib.sha224(line.encode()).hexdigest())
				fWrite.write("\n")
			fRead.close()
			fWrite.close()
			return '\nSe ha completado la traducción de hashes!\nArchivo guardado en: \n'
		elif op == '3':
			for line in fRead:
				fWrite.write(hashlib.sha256(line.encode()).hexdigest())
				fWrite.write("\n")
			fRead.close()
			fWrite.close()
			return '\nSe ha completado la traducción de hashes!\nArchivo guardado en: \n'
		elif op == '4':
			for line in fRead:
				fWrite.write(hashlib.sha384(line.encode()).hexdigest())
				fWrite.write("\n")
			fRead.close()
			fWrite.close()
			return '\nSe ha completado la traducción de hashes!\nArchivo guardado en: \n'
		elif op == '5':
			for line in fRead:
				fWrite.write(hashlib.sha512(line.encode()).hexdigest())
				fWrite.write("\n")
			fRead.close()
			fWrite.close()
			return '\nSe ha completado la traducción de hashes!\nArchivo guardado en: \n'
		elif op == '6':	
			for line in fRead:
				fWrite.write(hashlib.blake2b(line.encode()).hexdigest())
				fWrite.write("\n")
			fRead.close()
			fWrite.close()
			return '\nSe ha completado la traducción de hashes!\nArchivo guardado en: \n'
		elif op == '7':
			for line in fRead:
				fWrite.write(hashlib.blake2s(line.encode()).hexdigest())
				fWrite.write("\n")
			fRead.close()
			fWrite.close()
			return '\nSe ha completado la traducción de hashes!\nArchivo guardado en: \n'
		elif op == '8':
			for line in fRead:
				fWrite.write(hashlib.md5(line.encode()).hexdigest())
				fWrite.write("\n")
			fRead.close()
			fWrite.close()
			return '\nSe ha completado la traducción de hashes!\nArchivo guardado en: \n'
		else:
			print('Por favor, elija una opción correcta')
			selectOP(3)
			return traduct()
	except:
		return '\nNo se ha encontrado el archivo especificado'

def hashingFile():
	selectOP(1)
	print('\n1) SHA1')
	print('2) SHA224')
	print('3) SHA256')
	print('4) SHA384')
	print('5) SHA512')
	print('6) BLAKE2B')
	print('7) BLAKE2S')
	print('8) MD5')
	op = input('\nElija una opción: ')
	rutFile = input('Agrague la ruta del archivo del que desee calcular el Hash: ')

	if op == '1':
		try:
			hashsha1 = hashlib.sha1()
			with open(rutFile, "rb") as f:
				for block in iter(lambda: f.read(4096), b""):
					hashsha1.update(block)
					return hashsha1.hexdigest()
		except Exception as e:
			return f"Error: {e}"
	elif op == '2':
		try:
			hashsha224 = hashlib.sha224()
			with open(rutFile, "rb") as f:
				for block in iter(lambda: f.read(4096), b""):
					hashsha224.update(block)
					return hashsha224.hexdigest()
		except Exception as e:
			return f"Error: {e}"
	elif op == '3':
		try:
			hashsha256 = hashlib.sha256()
			with open(rutFile, "rb") as f:
				for block in iter(lambda: f.read(4096), b""):
					hashsha256.update(block)
					return hashsha256.hexdigest()
		except Exception as e:
			return f"Error: {e}"
	elif op == '4':
		try:
			hashsha384 = hashlib.sha384()
			with open(rutFile, "rb") as f:
				for block in iter(lambda: f.read(4096), b""):
					hashsha384.update(block)
					return hashsha384.hexdigest()
		except Exception as e:
			return f"Error: {e}"
	elif op == '5':
		try:
			hashsha512 = hashlib.sha512()
			with open(rutFile, "rb") as f:
				for block in iter(lambda: f.read(4096), b""):
					hashsha512.update(block)
					return hashsha512.hexdigest()
		except Exception as e:
			return f"Error: {e}"
	elif op == '6':
		try:
			hashblake2b = hashlib.blake2b()
			with open(rutFile, "rb") as f:
				for block in iter(lambda: f.read(4096), b""):
					hashblake2b.update(block)
					return hashblake2b.hexdigest()
		except Exception as e:
			return f"Error: {e}"
	elif op == '7':
		try:
			hashblake2s = hashlib.blake2s()
			with open(rutFile, "rb") as f:
				for block in iter(lambda: f.read(4096), b""):
					hashblake2s.update(block)
					return hashblake2s.hexdigest()
		except Exception as e:
			return f"Error: {e}"
	elif op == '8':
		try:
			hashmd5 = hashlib.md5()
			with open(rutFile, "rb") as f:
				for block in iter(lambda: f.read(4096), b""):
					hashmd5.update(block)
					return hashmd5.hexdigest()
		except Exception as e:
			return f"Error: {e}"
	else:
		print('Por favor, elija una opción correcta')
		selectOP(3)
		return hashingFile()

def menu():
	selectOP(1)
	print('\n1) Hash BruteForce')
	print('2) Hash Traductor')
	print('3) Calcular Hash Archivo')
	print('4) Salir\n')
	op = input('Seleccione una opción: ')

	if op == '1':
		try:
			response = hashBF()
			if response == None:
				print('\nNo se ha podido romper la clave')
			else:
				print(response)
		except:
			print('\nNo se ha encontrado el archivo especificado')
		options(1)
	elif op == '2':
		res = traduct()
		print(res)
		if res[1] == 'S':
			selectOP(2)
		options(2)
	elif op == '3':
		print(hashingFile())
		options(3)
	elif op == '4':
		selectOP(1)
		exit()
	else:
		print('¡Por favor, elija una opción correcta!')
		selectOP(3)
		menu()


if __name__ == '__main__':
	menu()