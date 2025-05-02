from src.helper.clear import clear
from src.controller.menu import menu
from src.controller.input_data import input_data
from src.controller.options import options

def main():
    while True:
        clear()
        menu()
        valor = input_data("Escolha uma opção: ")
        if valor == 5:
            print("👋 Saindo do programa... Até logo!")
            break
        options(valor)


if __name__ == "__main__":
    main()
