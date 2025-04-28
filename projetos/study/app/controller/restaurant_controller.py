from app.model.restaurante_model import restaurante_data

def create_restaurant():
    data = input('Informe o nome: ')
    restaurante_data.append(data)

def list_restaurants():
    print(restaurante_data)

