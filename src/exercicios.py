def calcular_lucro(receita, custo):
    return receita - custo


def calcular_margem(receita, custo):
    if receita == 0:
        return 0
    return (receita - custo) / receita * 100


def obter_dados():
    while True:
        try:
            receita = float(input("Digite a receita: "))
            custo = float(input("Digite o custo: "))
            return receita, custo
        except ValueError:
            print("Entrada invalida. Digite apenas numeros.")


while True:
    print("\n1 - Calcular lucro")
    print("2 - Ver margem")
    print("3 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        receita, custo = obter_dados()
        lucro = calcular_lucro(receita, custo)
        print("Lucro:", lucro)

    elif opcao == "2":
        receita, custo = obter_dados()
        margem = calcular_margem(receita, custo)
        print("Margem:", margem, "%")

    elif opcao == "3":
        print("Encerrando...")
        break

    else:
        print("Opcao invalida") 