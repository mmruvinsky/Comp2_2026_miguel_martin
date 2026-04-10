import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Lista archivos de un directorio (tipo ls simplificado)"
    )

    # argumento posicional opcional (directorio)
    parser.add_argument(
        "directorio",
        nargs="?",
        default=".",
        help="Directorio a listar (default: actual)"
    )

    # flag -a / --all
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Incluir archivos ocultos"
    )

    # filtro por extensión
    parser.add_argument(
        "--extension",
        help="Filtrar por extensión (ej: .txt)"
    )

    return parser.parse_args()


def listar(directorio, show_all=False, extension=None):
    resultado = []

    try:
        items = os.listdir(directorio)
    except FileNotFoundError:
        print(f"Error: el directorio '{directorio}' no existe.")
        return []
    except PermissionError:
        print(f"Error: sin permisos para acceder a '{directorio}'.")
        return []

    for item in items:
        # 🔹 ocultos
        if not show_all and item.startswith('.'):
            continue

        ruta = os.path.join(directorio, item)

        # 🔹 filtro extensión (solo para archivos)
        if extension and not item.endswith(extension):
            continue

        # 🔹 directorios con /
        if os.path.isdir(ruta):
            resultado.append(item + "/")
        else:
            resultado.append(item)

    return resultado


def main():
    args = parse_args()

    resultado = listar(
        args.directorio,
        show_all=args.all,
        extension=args.extension
    )

    if resultado:
        for item in resultado:
            print(item)
    else:
        print("No se encontraron archivos.")


if __name__ == "__main__":
    main()