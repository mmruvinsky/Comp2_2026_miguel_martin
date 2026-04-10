#!/usr/bin/env python3

import sys

def contar_lineas(argv):


    try:
        if len(argv) < 2:
            print("Uso: python wc_simple.py [archivo]")
            return

        archivo = argv[1]

        if archivo in ('-h', '--help'):
            print("Uso: python wc_simple.py [archivo]")
            print("Cuenta el número de líneas en el archivo proporcionado.")
            return
        else:
            with open(archivo, 'r') as f:
                return sum(1 for line in f)
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")


def main():
    lineas = contar_lineas(sys.argv)
    if lineas is not None:
      print(f"El archivo '{sys.argv[1]}' tiene {lineas} líneas.")
    else:     print("No se pudo contar las líneas.")
 

if __name__ == "__main__":
    main()