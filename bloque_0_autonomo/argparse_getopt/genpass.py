import secrets
import argparse
import string

def parse_args():
    parser = argparse.ArgumentParser(description="Genera una contraseña aleatoria segura")
    parser.add_argument("-n", "--largo", type=int, default=12, help="Longitud de la contraseña (default: 12)")
    parser.add_argument("-c", "--cantidad", type=int, default=1, help="Cantidad de contraseñas a generar (default: 1)")
    parser.add_argument("--no-symbols", "--ns", action="store_true", help="No incluir símbolos en la contraseña")
    parser.add_argument("--no-numbers", "--nn", action="store_true", help="No incluir números en la contraseña")
    parser.add_argument("--no-letters", "--nl", action="store_true", help="No incluir letras en la contraseña")
    return parser.parse_args()

def generar_contraseña(largo=12, no_symbols=False, no_numbers=False, no_letters=False):
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    contraseña = ""
    for i in range(largo):
        if no_symbols:
            caracteres = caracteres.replace(string.punctuation, "")
        if no_numbers:
            caracteres = caracteres.replace(string.digits, "")
        if no_letters:
            caracteres = caracteres.replace(string.ascii_letters, "")
        contraseña += secrets.choice(caracteres)
    return contraseña

import secrets
import argparse
import string


def parse_args():
    parser = argparse.ArgumentParser(
        description="Genera contraseñas seguras"
    )

    parser.add_argument("-n", "--largo", type=int, default=12)
    parser.add_argument("-c", "--cantidad", type=int, default=1)

    parser.add_argument("--no-symbols", "--ns", action="store_true")
    parser.add_argument("--no-numbers", "--nn", action="store_true")
    parser.add_argument("--no-letters", "--nl", action="store_true")

    return parser.parse_args()


def generar_contraseña(largo=12, no_symbols=False, no_numbers=False, no_letters=False):
    caracteres = ""

    if not no_letters:
        caracteres += string.ascii_letters

    if not no_numbers:
        caracteres += string.digits

    if not no_symbols:
        caracteres += string.punctuation

    # 🚨 validar
    if not caracteres:
        raise ValueError("No hay caracteres disponibles para generar la contraseña")

    # generar
    return ''.join(secrets.choice(caracteres) for _ in range(largo))


def main():
    args = parse_args()

    for _ in range(args.cantidad):
        try:
            print(
                generar_contraseña(
                    args.largo,
                    args.no_symbols,
                    args.no_numbers,
                    args.no_letters
                )
            )
        except ValueError as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()



    