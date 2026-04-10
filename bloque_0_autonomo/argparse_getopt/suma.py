#!/usr/bin/env python3
import sys


def main():
    nums = sys.argv[1:]

    if not nums:
        print("Suma: 0")
        return

    total = 0.0
    for num in nums:
        try:
            total += float(num)
        except ValueError:
            print(f"'{num}' no es un número válido y se ignorará.", file=sys.stderr)

    # Mostrar como int si no tiene decimales
    if total == int(total):
        print(f"Suma: {int(total)}")
    else:
        print(f"Suma: {total}")


if __name__ == "__main__":
    main()