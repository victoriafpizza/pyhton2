# Victoria Franceschini Pizza rm550609
def main():
    numero_zero = 0
    numeros_set = set([numero_zero])

    print("Digite o tipo numérico desejado (inteiro ou real): ")
    tipo_numerico = input().lower()

    while len(numeros_set) < 10:
        try:
            numero_digitado = input(f"Digite um número {tipo_numerico}: ")
            numero = None

            if tipo_numerico == "inteiro":
                numero = int(numero_digitado)
            elif tipo_numerico == "real":
                numero = float(numero_digitado)
            else:
                print("Tipo numérico inválido. Use 'inteiro' ou 'real'.")
                continue

            numeros_set.add(numero)

        except ValueError: 
            print("Valor inválido. Certifique-se de digitar um número válido.")

    numeros_set.remove(numero_zero)
    maior_numero = max(numeros_set)

    print(f"Tipo numérico escolhido: {tipo_numerico}")
    print(f"Maior valor do set: {maior_numero}")
    print(f"Valores do set: {numeros_set}")
    print(f"Tamanho do set: {len(numeros_set)}")

if __name__ == "__main__":
    main()
