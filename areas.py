import math

figura = input(
    "Ingrese la figura (circulo, rectangulo o triangulo): "
).lower()

if figura == "circulo":
    radio = float(input("Ingrese el radio: "))
    area = math.pi * radio ** 2
    print("El área del círculo es:", area)

elif figura == "rectangulo":
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area = base * altura
    print("El área del rectángulo es:", area)

elif figura == "triangulo":
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area = (base * altura) / 2
    print("El área del triángulo es:", area)

else:
    print("Figura no válida")
