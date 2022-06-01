import calculadora
if __name__ == "__main__":

    print("Selecciona una operacion:\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division")
    opcion = int(input("Opcion: "))

    if not opcion > 4:
        numero_1 = int(input("Primer numero: "))
        numero_2 = int(input("Segundo numero: "))
    
        if opcion == 1:
            calculadora.suma(numero_1, numero_2)
        elif opcion == 2:
            calculadora.resta(numero_1, numero_2)
        elif opcion == 3:
            calculadora.multiplicacion(numero_1, numero_2)
        elif opcion == 4:
            calculadora.division(numero_1, numero_2)
    else:
        print("Opcion Incorrecta")