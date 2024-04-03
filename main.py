def obtener_numero_positivo():
    """Solicita al usuario que ingrese un número positivo o 'T' para terminar."""
    while True:
        try:
            num_str = input("Ingresa un número positivo (o 'T' para terminar): ")
            if num_str.upper() == 'T':
                return 'T'  # Devuelve 'T' para indicar que se desea terminar el proceso
            num = int(num_str)
            if num < 0:
                print("Por favor, ingresa un número positivo mayor o igual a cero.")
            else:
                return num
        except ValueError:
            print("Por favor, ingresa un número entero válido o 'T' para terminar.")

# Bucle principal para solicitar números y calcular el MCD
while True:
    num1 = obtener_numero_positivo()
    if num1 == 'T':
        print("Has ingresado 'T' para terminar el proceso. El programa ha terminado.")
        break
    num2 = obtener_numero_positivo()
    if num2 == 'T':
        print("Has ingresado 'T' para terminar el proceso. El programa ha terminado.")
        break
    resultado = mcd(num1, num2)
    print("El máximo común divisor de", num1, "y", num2, "es:", resultado)
