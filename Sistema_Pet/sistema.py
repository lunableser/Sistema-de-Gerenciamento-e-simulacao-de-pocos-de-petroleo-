# SISTEMA DE GERENCIAMENTO E SIMULAÇÃO DE POÇOS DE PETRÓLEO EM PYTHON
# sistema.py - define as funções de cadastro, login, produção...

from poco import Poco

# Busca um poço pelo ID dentro da lista de poços
def buscar_poco(pocos, id_poco):
    for poco in pocos:
        if poco.id == id_poco:
            return poco
    return None

# Cadastro de um novo poço
def cadastrar_poco(pocos):

    id_poco = input("Digite o ID do poço: ")

    # O ID ADMIN é reservado para o gerente
    if id_poco == "ADMIN":
        print("Esse ID é reservado!")
        return
    
    # Verifica se o ID já existe
    if buscar_poco(pocos, id_poco):
        print("Esse ID já está cadastrado!")
        return

    campo = input("Digite o campo do poço: ")

    try:
        declinio = float(input("Digite a taxa de declínio anual (%): "))
        producao = float(input("Digite a produção acumulada inicial (bbl): "))

        # Evita valores inválidos
        if declinio < 0 or producao < 0:
            print("Valores não podem ser negativos!")
            return

    except ValueError:
        print("Digite apenas valores numéricos!")
        return

    senha = input("Digite a senha do operador: ")

    # O declínio é armazenado como decimal.
    # Exemplo: 5% vira 0.05
    novo_poco = Poco(
        id_poco,
        campo,
        declinio / 100,
        senha,
        producao
    )

    # Adiciona o novo poço ao banco de dados
    pocos.append(novo_poco)

    print("\nPoço cadastrado com sucesso!")

# Login do operador ou administrador
def login(pocos):

    id_usuario = input("ID: ")
    senha = input("Senha: ")

    # Login do gerente
    if id_usuario == "ADMIN" and senha == "admin123":
        return "ADMIN"

    # Procura o poço
    poco = buscar_poco(pocos, id_usuario)

    if poco and poco.senha == senha:
        return poco

    print("Login inválido!")
    return None

# Mostra informações do poço logado
def mostrar_status(poco):

    print("\n--- STATUS DO POÇO ---")
    print("ID:", poco.id)
    print("Campo:", poco.campo)
    print("Taxa de declínio:", poco.declinio * 100, "%")
    print("Produção acumulada:", poco.producao, "bbl")
    print("----------------------")

# Registra produção diária
def registrar_producao(poco):

    print("\n--- REGISTRO DE PRODUÇÃO ---")

    try:
        volume = float(input("Informe a produção diária (bbl): "))

        if volume <= 0:
            print("A produção deve ser maior que zero!")
            return

    except ValueError:
        print("Digite apenas valores numéricos!")
        return

    # Soma a produção diária na produção acumulada
    poco.producao += volume

    print("\nProdução registrada com sucesso!")
    print("Produção atual:", poco.producao, "bbl")

# Transfere volume de um poço para outro
def transferir_volume(pocos, origem):

    print("\n--- TRANSFERÊNCIA DE VOLUME ---")

    destino_id = input("ID do poço destino: ")

    destino = buscar_poco(pocos, destino_id)

    if destino is None:
        print("Poço destino não encontrado!")
        return

    try:
        volume = float(input("Quantidade de barris: "))

    except ValueError:
        print("Digite apenas valores numéricos!")
        return

    if volume <= 0:
        print("O volume deve ser maior que zero!")
        return

    if volume > origem.producao:
        print("Volume maior que a produção disponível!")
        return

    origem.producao -= volume
    destino.producao += volume

    print("\nTransferência realizada!")

# Previsão de produção usando declínio exponencial
def calcular_declinio(poco):

    print("\n--- PREVISÃO DE DECLÍNIO ---")

    # Fórmula:
    # P = P0 * (1 - d)^t
    #
    # P0 = produção inicial
    # d = taxa de declínio
    # t = tempo em anos

    for ano in range(1, 6):

        producao = poco.producao * ((1 - poco.declinio) ** ano)

        print(f"Ano {ano}: {producao:.2f} bbl")

# Relatório geral para o administrador
def relatorio_campo(pocos):

    print("\n" + "-" * 50)
    print("        RELATÓRIO GERAL DO CAMPO")
    print("-" * 50)

    if len(pocos) == 0:
        print("Nenhum poço cadastrado.")
        return

    for poco in pocos:

        print("\nID do poço:", poco.id)
        print("Campo:", poco.campo)
        print("Taxa de declínio:", poco.declinio * 100, "%")
        print("Produção acumulada:", f"{poco.producao:.2f}", "bbl")
        print("-" * 50)

# Remove um poço do sistema
def remover_poco(pocos):

    id_poco = input("ID do poço para remover: ")

    poco = buscar_poco(pocos, id_poco)

    if poco is None:
        print("Poço não encontrado!")
        return

    confirma = input("Confirmar remoção? (s/n): ")

    if confirma.lower() != "s":
        print("Operação cancelada!")
        return

    pocos.remove(poco)

    print("Poço removido com sucesso!")
