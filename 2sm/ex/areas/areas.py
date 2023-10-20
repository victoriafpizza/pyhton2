# Evitar inputs em funções

# Função cálculo o retângulo
def area_retangulo(lado,altura):
    return lado * altura

# Função cálculo do triângulo
def area_triangulo(lado,altura):
    return lado * altura / 2

# Função cálculo o circulo
def area_circulo(raio):
    import math
    return math.pi * math.pow(raio, 2)