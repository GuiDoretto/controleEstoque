#Nome: Guilherme Doretto Sobreiro RM:99674
#Nome: Matheus Xavier Silva de Toledo RM:98423
#Nome: Samyr Tatoni Kotait RM:99629

import sys

compras = []
estoque = []

# Definir uma classe para representar os vinhos
class Vinho:
    def __init__(self, descricao, quantidade):
        self.descricao = descricao
        self.quantidade = quantidade

# Função para exibir o menu principal
def menu_principal():
    print("===== MENU PRINCIPAL =====")
    print("1. Compras")
    print("2. Estoque")
    print("3. Sair")
    print("==========================")

# Função para exibir o menu de compras
def menu_compras():
    print("===== MENU COMPRAS =====")
    print("1. Cadastrar compra")
    print("2. Mostrar todas as compras")
    print("3. Voltar ao menu principal")
    print("=========================")

# Função para exibir o menu de estoque
def menu_estoque():
    print("===== MENU ESTOQUE =====")
    print("1. Registrar entrada no estoque")
    print("2. Registrar saída do estoque")
    print("3. Mostrar estoque")
    print("4. Voltar ao menu principal")
    print("=========================")

# Função para cadastrar uma compra
def cadastrar_compra():
    descricao = input("Digite a descrição da compra: ")
    quantidade = int(input("Digite a quantidade comprada: "))
    valor = float(input("Digite o valor unitário: "))
    compras.append((descricao, quantidade, valor))
    print("Compra cadastrada com sucesso!")

# Função para mostrar todas as compras
def mostrar_compras():
    if not compras:
        print("Nenhuma compra cadastrada.")
    else:
        print("===== LISTA DE COMPRAS =====")
        for compra in compras:
            print("Descrição:", compra[0])
            print("Quantidade:", compra[1])
            print("Valor unitário:", compra[2])
            print("============================")

# Função para registrar uma entrada no estoque
def registrar_entrada():
    print("===== VINHOS DISPONÍVEIS =====")
    for i, vinho in enumerate(estoque, start=1):
        print(f"{i}. {vinho.descricao}")
    print("============================")
    opcao = int(input("Selecione o vinho para a entrada: "))
    vinho_selecionado = estoque[opcao-1]
    quantidade = int(input("Digite a quantidade recebida: "))
    vinho_selecionado.quantidade += quantidade
    print("Entrada registrada no estoque com sucesso!")

# Função para registrar uma saída do estoque
def registrar_saida():
    print("===== VINHOS DISPONÍVEIS =====")
    for i, vinho in enumerate(estoque, start=1):
        print(f"{i}. {vinho.descricao}")
    print("============================")
    opcao = int(input("Selecione o vinho para a saída: "))
    vinho_selecionado = estoque[opcao-1]
    quantidade = int(input("Digite a quantidade vendida: "))
    if quantidade <= vinho_selecionado.quantidade:
        vinho_selecionado.quantidade -= quantidade
        print("Saída registrada no estoque com sucesso!")
    else:
        print("Quantidade insuficiente no estoque.")

# Função para mostrar o estoque
def mostrar_estoque():
    if not estoque:
        print("Estoque vazio.")
    else:
        print("===== ESTOQUE =====")
        for i, vinho in enumerate(estoque, start=1):
            print(f"{i}. {vinho.descricao} - Quantidade: {vinho.quantidade}")
        print("===================")

# Função para selecionar a opção do menu principal
def selecionar_opcao_principal(opcao):
    match opcao:
        case 1:
            while True:
                menu_compras()
                opcao_compras = int(input("Digite sua opção: "))

                match opcao_compras:
                    case 1:
                        cadastrar_compra()
                    case 2:
                        mostrar_compras()
                    case 3:
                        break
                    case _:
                        print("Opção inválida. Por favor, tente novamente.")

        case 2:
            while True:
                menu_estoque()
                opcao_estoque = int(input("Digite sua opção: "))

                match opcao_estoque:
                    case 1:
                        registrar_entrada()
                    case 2:
                        registrar_saida()
                    case 3:
                        mostrar_estoque()
                    case 4:
                        break
                    case _:
                        print("Opção inválida. Por favor, tente novamente.")

        case 3:
            print("Encerrando o programa...")
            sys.exit()

        case _:
            print("Opção inválida. Por favor, tente novamente.")

# Adicionar vinhos ao estoque
estoque.append(Vinho("Vinho Tinto", 10))
estoque.append(Vinho("Vinho Branco", 15))
estoque.append(Vinho("Vinho Rosé", 20))
estoque.append(Vinho("Vinho Espumante", 5))
estoque.append(Vinho("Vinho do Porto", 8))

# Loop principal do programa
while True:
    menu_principal()
    opcao_principal = int(input("Digite sua opção: "))
    selecionar_opcao_principal(opcao_principal)