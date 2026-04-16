#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Error: Debe especificar un archivo")
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        with open(archivo, 'r') as f:
            lineas = sum(1 for _ in f)
        print(f"{lineas} líneas")
    except FileNotFoundError:
        print(f"Error: No se puede leer '{archivo}'")
        sys.exit(1)
    except PermissionError:
        print(f"Error: No se puede leer '{archivo}'")
        sys.exit(1)

if __name__ == "__main__":
    main()