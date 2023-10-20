# puxar de um arquivo para o outro (na mesma pasta
import areas

print("Escolha")
print("(1) Área do triângulo")
print("(2) Área do retângulo")
print("(3) Área do círculo")
escolha = int(input("Escolha: "))

if escolha == 1:
    lado = float(input("Digite o lado: "))
    altura = float(input("Digite a altura: "))
               # Puzando do outro arquivo (nome.funçaõ())
    resultado = areas.area_retangulo()
    print(f"Resultado: {resultado:.2f}")
elif escolha == 2:
    lado = float(input("Digite o lado: "))
    altura = float(input("Digite a altura: "))
    resultado = areas.area_triangulo()
    print(f"Resultado: {resultado:.2f}")
elif escolha == 3:
    raio = float(input("Digite o raio: "))
    resultado = areas.area_circulo()
    print(f"Resultado: {resultado:.2f}")
else:
    print("Digite uma opção válida")