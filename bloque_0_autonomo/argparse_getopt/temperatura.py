#!/usr/bin/env python3

import argparse

def parser():
    parser = argparse.ArgumentParser(description="Convierte temperaturas entre Celsius y Fahrenheit")
    parser.add_argument("temperatura", type=float, help="Valor de la temperatura a convertir")
    parser.add_argument("--to", choices=['celsius', 'fahrenheit'], required=True, help="Unidad a convertir: 'celsius' o 'fahrenheit'")
    return parser.parse_args()

def conversor():
    args = parser()
    if args.to == 'celsius':

        resultado = (args.temperatura - 32) * 5.0/9.0
        print(f"{args.temperatura}°F es igual a {resultado:.2f}°C")
    elif args.to == 'fahrenheit':
        resultado = (args.temperatura * 9.0/5.0) + 32
        print(f"{args.temperatura}°C es igual a {resultado:.2f}°F")
    else:
        print("Por favor, elige una opción de conversión: --to celsius o --to fahrenheit")

def main():
    conversor()
    print("¡Conversión completada!")

if __name__ == "__main__":    main()