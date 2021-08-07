cardapio = "Lasanha: 8.00\nEstrogonofe: 11.00\nRefrigerante: 3.00\nSuco: 2.50"
produtos = {"lasanha": 8.00, "estrogonofe": 11.00, "refrigerante": 3.00, "suco": 2.50}


def restaurante(valor):
    print("Escolha seu pedido")
    print(cardapio)
    opcao_um = input("escolha lasanha ou estrogonofe:")
    opcao_um = opcao_um.lower()
    if opcao_um == "lasanha":
        valor = produtos.get("lasanha", 'produto nao tabelado')

    elif opcao_um == "estrogonofe":
        valor = produtos.get("estrogonofe", 'produto nao tabelado')

    else:
        print("opcao invalida")
        restaurante(0)

    opcao_dois = input("escolha refrigerante ou suco:")
    opcao_dois = opcao_dois.lower()
    if opcao_dois == "refrigerante":
        valor += produtos.get("refrigerante", 'produto nao tabelado')

    elif opcao_dois == "suco":
        valor += produtos.get("suco", 'produto nao tabelado')

    else:
        print("opcao invalida")
        restaurante(0)
    print(f"seu pedido foi {opcao_um} e um {opcao_dois}, totalizando: {valor}")

    print(f"Deseja fazer mais algum pedido? [S/N]")

    if input().lower() == "s":
        restaurante(valor)
    elif input().lower() == "n":
        print("obrigado pela preferencia, ate mais")


if __name__ == '__main__':
    restaurante(0)
