restaurantes = []

def store(data):
    restaurantes.append(
        {"nome": data, "status": False}
    )


def show():
    for idx, restaurant in enumerate(restaurantes, start=1):
        if restaurant["status"]:
            print(f"{idx}. {restaurant['nome']}")


def active(nome):
    for restaurante in restaurantes:
        if restaurante["nome"] == nome:
            restaurante["status"] = True            
            return
    input(f"\n❌ Restaurante '{nome}' não encontrado. Pressione Enter para voltar ao menu...")

def edit(nome):
    for restaurante in restaurantes:
        if restaurante["nome"] == nome:
            novo_nome = input("Informe o novo nome do restaurante: ")
            restaurante["nome"] = novo_nome
            print(f"✅ Restaurante '{nome}' atualizado para '{novo_nome}'.")
            return                    
    input(f"\n❌ Restaurante: {nome}  não encontrado. Pressione Enter para voltar ao menu...")                   
