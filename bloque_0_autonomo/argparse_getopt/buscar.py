import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Grep simplificado")

    parser.add_argument("pattern", type=str, help="Patrón a buscar")

    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType('r'),
        help="Archivo en el que buscar"
    )

    parser.add_argument("-i", "--ignore-case", action="store_true", help="Ignorar mayúsculas/minúsculas")
    parser.add_argument("-n", "--line-number", action="store_true", help="Mostrar número de línea")
    parser.add_argument("-c", "--count", action="store_true", help="Solo mostrar el número de coincidencias")
    parser.add_argument("-v", "--invert-match", action="store_true", help="Invertir coincidencia")

    return parser.parse_args()


def grep(pattern, file, ignore_case, line_number, count, invert_match):
    try:
        matches = 0

        for i, line in enumerate(file, start=1):

            text = line
            pat = pattern

            if ignore_case:
                text = text.lower()
                pat = pat.lower()

            found = pat in text

            if invert_match:
                found = not found

            if found:
                matches += 1

                if not count:
                    if line_number:
                        print(f"{i}:{line}", end='')
                    else:
                        print(line, end='')

        if count:
            print(matches)

    except Exception as e:
        print(f"Error: {e}")


def main():
    args = parse_args()

    if args.file:
        grep(
            args.pattern,
            args.file,
            args.ignore_case,
            args.line_number,
            args.count,
            args.invert_match
        )
    else:
        if not sys.stdin.isatty():
            grep(
                args.pattern,
                sys.stdin,
                args.ignore_case,
                args.line_number,
                args.count,
                args.invert_match
            )
        else:
            print("Error: tenés que pasar un archivo o usar stdin (pipe)")


if __name__ == "__main__":
    main()