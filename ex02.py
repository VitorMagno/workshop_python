cardapio = "Lasanha: 8.00\nEstrogonofe: 11.00\nRefrigerante: 3.00\nSuco: 2.50"


def restaurante(valor):
    print("Escolha seu pedido")
    print(cardapio)
    opcao_um = input("escolha lasanha ou estrogonofe:")
    opcao_um = opcao_um.lower()
    if opcao_um == "lasanha":
        valor = 8.00
    elif opcao_um == "estrogonofe":
        valor = 11.00
    else:
        print("opcao invalida")
        restaurante(0)

    opcao_dois = input("escolha refrigerante ou suco:")
    opcao_dois = opcao_dois.lower()
    if opcao_dois == "refrigerante":
        valor += 3.00
    elif opcao_dois == "suco":
        valor += 2.50
    else:
        print("opcao invalida")
        restaurante(0)
    print(f"seu pedido foi {opcao_um} e um {opcao_dois}, totalizando: {valor}")

    print(f"Deseja fazer mais algum pedido? [S/N]")

    if input().lower() == "s":
        restaurante(valor)
    elif input().lower() == "n":
        print("obrigado pela preferencia, ate mais")
        breakpoint()


if __name__ == '__main__':
    restaurante(0)
