from src.controller.input_data import input_data
from src.controller.menu import menu
from src.controller.options import options
from src.helper.clear import clear


def main():
    while True:
        clear()
        menu()
        valor = input_data("Escolha uma opção: ")
        if valor == 4:
            print("👋 Saindo do programa... Até logo!")
            break
        options(valor)


if __name__ == "__main__":
    main()
