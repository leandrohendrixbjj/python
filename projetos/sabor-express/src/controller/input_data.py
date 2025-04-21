def input_data(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("❌ Por favor, digite um número inteiro válido.")
