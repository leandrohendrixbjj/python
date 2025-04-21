from src.controller.options import options


def selecao_menu():
    opcoes_list = [1, 2, 3, 4]
    opcao_selecionada = int(input('Escolha uma opção:'))

    if not opcao_selecionada in opcoes_list:
        print(f"Opção {opcao_selecionada} não consta na lista!")
    else:
        options(opcao_selecionada)
