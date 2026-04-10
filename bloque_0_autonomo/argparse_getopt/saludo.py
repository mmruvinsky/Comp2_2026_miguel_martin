#!/usr/bin/env python3
import sys


def main():
    if len(sys.argv) < 2:
        print("Uso: saludo.py <nombre>")
        sys.exit(1)

    nombre = " ".join(sys.argv[1:])
    print(f"Hola, {nombre}!")


if __name__ == "__main__":
    main()