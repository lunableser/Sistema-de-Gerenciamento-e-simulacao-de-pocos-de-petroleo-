# SISTEMA DE GERENCIAMENTO E SIMULAÇÃO DE POÇOS DE PETRÓLEO EM PYTHON
# main.py - controla o fluxo principal do programa

from sistema import (
    cadastrar_poco,
    login,
    mostrar_status,
    registrar_producao,
    transferir_volume,
    calcular_declinio,
    relatorio_campo,
    remover_poco
)

# Menu do engenheiro de campo
def menu_operador(pocos, poco_logado):

    while True:

        print("""
--- MENU DO OPERADOR ---

1 - Ver status do poço
2 - Registrar produção diária
3 - Transferir volume
4 - Previsão de declínio
5 - Logoff
""")

        opcao = input("Escolha: ")

        if opcao == "1":

            mostrar_status(poco_logado)

        elif opcao == "2":

            registrar_producao(poco_logado)

        elif opcao == "3":

            transferir_volume(
                pocos,
                poco_logado
            )

        elif opcao == "4":
            calcular_declinio(poco_logado)

        elif opcao == "5":
            print("Saindo da conta...")
            break

        else:
            print("Opção inválida!")

# Menu do gerente
def menu_admin(pocos):

    while True:

        print("""
--- MENU GERENTE ---

1 - Relatório geral do campo
2 - Remover poço
3 - Logoff
""")

        opcao = input("Escolha: ")

        if opcao == "1":

            relatorio_campo(pocos)

        elif opcao == "2":

            remover_poco(pocos)

        elif opcao == "3":

            print("Saindo da conta...")

            break

        else:

            print("Opção inválida!")

# Programa principal
def main():

    # Banco de dados dos poços
    pocos = []

    while True:

        print("""
========================
        PetroPy
========================

1 - Cadastrar novo poço
2 - Autenticar operador
3 - Encerrar sistema
""")

        opcao = input("Escolha: ")

        if opcao == "1":

            cadastrar_poco(pocos)

        elif opcao == "2":

            usuario = login(pocos)

            if usuario == "ADMIN":

                menu_admin(pocos)

            elif usuario is not None:

                menu_operador(
                    pocos,
                    usuario
                )

        elif opcao == "3":

            print("Sistema encerrado!")

            break

        else:

            print("Opção inválida!")

# Executa o programa
main()