import sys

def main():
    nums = sys.argv[1:]
    sum = 0
    for num in nums:
        if num.isdigit():
            sum += int(num)
        elif num == '-h' or num == '--help':
            print("Uso: python suma.py [números]")
            print("Suma los números proporcionados como argumentos.")
            return
        else:
            print(f"'{num}' no es un número válido y se ignorará.")
    print(f"La suma es: {sum}")

if __name__ == "__main__":    main()
