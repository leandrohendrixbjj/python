from src.model.restaurantes import store, show, edit


def options(input_data: int):
    match input_data:
        case 1:
            print('➕ Cadastrar um Restaurante')
            nome = input('Informe o nome do Restaurante: ')
            store(nome)
        case 2:
            show()
            input("\nPressione Enter para voltar ao menu...")
        case 3:
            print('🚧 Ativar um Restaurante (em construção)')
            nome = input('Informe o nome do Restaurante: ')
            edit(nome)
        case _:
            print(f"❌ Opção {input_data} inválida")
