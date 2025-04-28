from app.infra.clear import clear
from app.model.menu import menu
from app.controller.seek_controller import seek
optionsList = ['1','2','3','4']

def main():
    while True:
        clear()
        menu()
        option = input("Select an option: ")

        if not option in optionsList:
            print('Please select an option from the list')
            input("Enter select item from list option: ")
            continue
        seek(option)



if __name__ == '__main__':
    main()