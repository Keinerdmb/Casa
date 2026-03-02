
#CALCULDAORA EN PYTHON

def suma (a, b):
    return a + b
def resta (a, b):
    return a - b
def multiplicacion (a, b):
    return a * b 
def division (a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"
def potencia (a, b):
    return a ** b 
def raiz_cuadrada (a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
def porcentaje (a, b):
    return (a * b) / 100
def modulo (a, b):
    if b != 0:
        return a % b
    else:
        return "No se puede calcular el módulo por cero"
def promedio (a, b):
    return (a + b) / 2

def menu():
  while True:
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Porcentaje")
    print("8. Módulo")
    print("9. Promedio")
    print("0. Salir")

    opcion = input ("ingrese el número de la operación a realizar:")
    
    if opcion == "1":
        a = float(input("Ingrese el primer número:"))
        b = float(input("Ingrese el segundo número:"))
        print("El resultado de la suma es:", suma(a, b))
    elif opcion == "2":
        a = float(input("Ingrese el primer número:"))
        b = float(input("Ingrese el segundo número:"))
        print("El resultado de la resta es:", resta(a, b))
    elif opcion == "3":
        a = float(input("Ingrese el primer número:"))
        b = float(input("Ingrese el segundo número:"))
        print("El resultado de la multiplicación es:", multiplicacion(a, b))
    elif opcion == "4": 
        a = float(input("Ingrese el primer número:"))
        b = float(input("Ingrese el segundo número:"))
        print("El resultado de la división es:", division(a, b))
    elif opcion == "5":
        a = float(input("Ingrese el número base:"))
        b = float(input("Ingrese el número exponente:"))
        print("El resultado de la potencia es:", potencia(a, b))
    elif opcion == "6":
        a = float(input("Ingrese el número:"))
        print("El resultado de la raíz cuadrada es:", raiz_cuadrada(a))
    elif opcion == "7":
        a = float(input("Ingrese el número:"))
        b = float(input("Ingrese el porcentaje:"))
        print("El resultado del porcentaje es:", porcentaje(a, b))
    elif opcion == "8":
        a = float(input("Ingrese el primer número:"))
        b = float(input("Ingrese el segundo número:"))
        print("El resultado del módulo es:", modulo(a, b))
    elif opcion == "9": 
        a = float(input("Ingrese el primer número:"))
        b = float(input("Ingrese el segundo número:"))
        print("El resultado del promedio es:", promedio(a, b))
    elif opcion == "0":
        print("¡Gracias por usar la calculadora!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")


            

        
menu()