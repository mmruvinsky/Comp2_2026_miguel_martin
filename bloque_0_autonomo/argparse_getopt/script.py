import argparse

parser = argparse.ArgumentParser(description="Procesa un archivo de texto")
parser.add_argument("archivo", help="Archivo a procesar")
parser.add_argument("-v", "--verbose", action="store_true", help="Modo detallado")
parser.add_argument("-n", "--lineas", type=int, default=10, help="Número de líneas")

args = parser.parse_args()

print(f"Procesando {args.archivo}")
print(f"Verbose: {args.verbose}")
print(f"Líneas: {args.lineas}")