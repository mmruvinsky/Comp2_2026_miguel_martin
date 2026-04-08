#!/usr/bin/env python3

import argparse

def crear_parser():
    parser = argparse.ArgumentParser(description="suma números")
    parser.add_argument(
        "numeros",
        nargs="*",          # 0 o más valores
        type=float,         # convertir a número (float)
        help="Números a sumar"
    )
    return parser

def main():
    parser = crear_parser()
    try:
        args = parser.parse_args()
    except SystemExit as e:
        print(f"Error: Solo se permiten números. {e}")
        return

    total = sum(args.numeros)
    print(f"Suma: {total}")


if __name__ == "__main__":
    main()
