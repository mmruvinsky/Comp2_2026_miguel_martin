#!/usr/bin/env python3
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Grep simplificado: busca un patrón en archivos o stdin"
    )
    parser.add_argument(
        "pattern",
        type=str,
        help="Patrón de texto a buscar"
    )
    parser.add_argument(
        "files",
        nargs="*",
        type=argparse.FileType('r'),
        help="Archivos en los que buscar (si no se indica, lee de stdin)"
    )
    parser.add_argument(
        "-i", "--ignore-case",
        action="store_true",
        help="Ignorar mayúsculas/minúsculas"
    )
    parser.add_argument(
        "-n", "--line-number",
        action="store_true",
        help="Mostrar número de línea antes de cada coincidencia"
    )
    parser.add_argument(
        "-c", "--count",
        action="store_true",
        help="Mostrar solo el número de coincidencias por archivo"
    )
    parser.add_argument(
        "-v", "--invert-match",
        action="store_true",
        help="Mostrar las líneas que NO coinciden con el patrón"
    )
    return parser.parse_args()


def grep(pattern, file, filename, ignore_case, line_number, count, invert_match, show_filename):
    """Busca pattern en file. Retorna el número de coincidencias encontradas."""
    matches = 0
    pat = pattern.lower() if ignore_case else pattern

    for i, line in enumerate(file, start=1):
        text = line.lower() if ignore_case else line
        found = pat in text

        if invert_match:
            found = not found

        if not found:
            continue

        matches += 1

        if not count:
            parts = []
            if show_filename:
                parts.append(filename)
            if line_number:
                parts.append(str(i))
            if parts:
                print(":".join(parts) + ":", end="")
            print(line, end="")

    return matches


def main():
    args = parse_args()

    # Decidir fuente de datos
    if args.files:
        fuentes = [(f, f.name) for f in args.files]
    elif not sys.stdin.isatty():
        fuentes = [(sys.stdin, "<stdin>")]
    else:
        print("Error: pasá un archivo o usá stdin (pipe)", file=sys.stderr)
        sys.exit(1)

    # Con múltiples archivos se muestra el nombre del archivo por defecto
    show_filename = len(fuentes) > 1

    total = 0
    errores = False

    for file, filename in fuentes:
        try:
            matches = grep(
                pattern=args.pattern,
                file=file,
                filename=filename,
                ignore_case=args.ignore_case,
                line_number=args.line_number,
                count=args.count,
                invert_match=args.invert_match,
                show_filename=show_filename,
            )
            if args.count:
                print(f"{filename}: {matches} coincidencias")
            total += matches
        except OSError as e:
            print(f"Error al leer '{filename}': {e}", file=sys.stderr)
            errores = True
        finally:
            if file is not sys.stdin:
                file.close()

    if args.count and len(fuentes) > 1:
        print(f"Total: {total} coincidencias")

    if errores:
        sys.exit(2)
    sys.exit(0 if total > 0 else 1)


if __name__ == "__main__":
    main()