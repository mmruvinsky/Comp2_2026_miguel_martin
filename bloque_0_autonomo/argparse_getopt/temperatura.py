#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Convierte temperaturas entre Celsius y Fahrenheit")
    parser.add_argument("valor", type=float, help="Temperatura a convertir")
    parser.add_argument("-t", "--to", choices=['celsius', 'fahrenheit'], required=True, help="Unidad de destino")
    args = parser.parse_args()

    if args.to == 'fahrenheit':
        resultado = (args.valor * 9.0/5.0) + 32
        print(f"{args.valor}°C = {resultado:.1f}°F")
    else:
        resultado = (args.valor - 32) * 5.0/9.0
        print(f"{args.valor}°F = {resultado:.1f}°C")

if __name__ == "__main__":
    main()