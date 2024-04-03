def mcd(a, b):
    # Manejar el caso en que ambos números son cero
    if a == 0 and b == 0:
        return None

    # Algoritmo de Euclides para calcular el MCD
    while b:
        a, b = b, a % b
    return a


def obtener_numero_positivo():
    while True:
        try:
            num = int(input("Ingresa un número positivo (o ingresa 0 para terminar): "))
            if num < 0:
                print("Por favor, ingresa un número positivo.")
            else:
                return num
        except ValueError:
            print("Por favor, ingresa un número entero válido.")


# Solicitar números hasta que se ingrese uno positivo
num1 = obtener_numero_positivo()
if num1 == 0:
    print("Has ingresado 0 como primer número. El programa ha terminado.")
else:
    num2 = obtener_numero_positivo()
    if num2 == 0:
        print("Has ingresado 0 como segundo número. El programa ha terminado.")
    else:
        resultado = mcd(num1, num2)
        if resultado is None:
            print("No hay máximo común divisor cuando ambos números son 0.")
        else:
            print("El máximo común divisor de", num1, "y", num2, "es:", resultado)
