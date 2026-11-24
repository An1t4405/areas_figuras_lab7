"""Calculadora de áreas de figuras geométricas (versión refactorizada).

Refactorización pura: mismas preguntas, mismos mensajes y mismos resultados
que areas_antes.py; solo cambia la organización del código.
"""
import math


def pedir_numero(mensaje):
    """Pide un número decimal al usuario."""
    return float(input(mensaje))


def area_circulo(radio):
    """Área del círculo: π · r²."""
    return math.pi * radio ** 2


def area_rectangulo(base, altura):
    """Área del rectángulo: base · altura."""
    return base * altura


def area_triangulo(base, altura):
    """Área del triángulo: (base · altura) / 2."""
    return (base * altura) / 2


def pedir_base_y_altura():
    """Pide los dos datos que comparten el rectángulo y el triángulo."""
    base = pedir_numero("Ingrese la base: ")
    altura = pedir_numero("Ingrese la altura: ")
    return base, altura


def calcular_circulo():
    return area_circulo(pedir_numero("Ingrese el radio: "))


def calcular_rectangulo():
    return area_rectangulo(*pedir_base_y_altura())


def calcular_triangulo():
    return area_triangulo(*pedir_base_y_altura())


# Nombre que se muestra y función que calcula, según la figura elegida.
FIGURAS = {
    "circulo": ("círculo", calcular_circulo),
    "rectangulo": ("rectángulo", calcular_rectangulo),
    "triangulo": ("triángulo", calcular_triangulo),
}


def main():
    figura = input(
        "Ingrese la figura (circulo, rectangulo o triangulo): "
    ).lower()

    if figura not in FIGURAS:
        print("Figura no válida")
        return

    nombre, calcular = FIGURAS[figura]
    print(f"El área del {nombre} es:", calcular())


if __name__ == "__main__":
    main()
