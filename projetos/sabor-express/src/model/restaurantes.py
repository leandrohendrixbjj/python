restaurantes = []


def store(data):
    restaurantes.append(
        {"nome": data, "status": False}
    )


def show():
    for idx, restaurant in enumerate(restaurantes, start=1):
        if restaurant["status"]:
            print(f"{idx}. {restaurant['nome']}")


def edit(nome):
    for restaurante in restaurantes:
        if restaurante["nome"] == nome:
            restaurante["status"] = True
            restaurante["nome"] = nome
            print(f"✅ Restaurante '{nome}' ativado com sucesso!")
            return
    print(f"❌ Restaurante '{nome}' não encontrado.")
